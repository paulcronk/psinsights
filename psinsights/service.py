###############################################################################
# Copyright 2012 FastSoft Inc.
# Copyright 2012 Devin Anderson <danderson (at) fastsoft (dot) com>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License.  You may obtain a copy
# of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the
# License for the specific language governing permissions and limitations under
# the License.
###############################################################################

from httplib import HTTPSConnection as _HTTPSConnection
from json import loads as _loads
from socket import _GLOBAL_DEFAULT_TIMEOUT
from urllib import urlencode as _urlencode

from psinsights.analysis import Analysis as _Analysis
from psinsights.error import Error as _Error

class Service(object):

    # Supported locales
    # (https://developers.google.com/speed/docs/insights/languages)
    LOCALE_ARABIC = "ar"
    LOCALE_BULGARIAN = "bg"
    LOCALE_CATALAN = "ca"
    LOCALE_CHINESE_SIMPLIFIED = "zh_CN"
    LOCALE_CHINESE_TRADITIONAL = "zh_TW"
    LOCALE_CROATIAN = "hr"
    LOCALE_CZECH = "cs"
    LOCALE_DANISH = "da"
    LOCALE_DUTCH = "nl"
    LOCALE_ENGLISH = "en"
    LOCALE_ENGLISH_UK = "en_GB"
    LOCALE_ENGLISH_US = "en_US"
    LOCALE_FILIPINO = "fil"
    LOCALE_FINNISH = "fi"
    LOCALE_FRENCH = "fr"
    LOCALE_GERMAN = "de"
    LOCALE_GREEK = "el"
    LOCALE_HEBREW = "iw"
    LOCALE_HINDI = "hi"
    LOCALE_HUNGARIAN = "hu"
    LOCALE_INDONESIAN = "id"
    LOCALE_ITALIAN = "it"
    LOCALE_JAPANESE = "ja"
    LOCALE_KOREAN = "ko"
    LOCALE_LATVIAN = "lv"
    LOCALE_LITHUANIAN = "lt"
    LOCALE_NORWEGIAN = "no"
    LOCALE_POLISH = "pl"
    LOCALE_PORTUGUESE_BRAZILIAN = "pt_BR"
    LOCALE_PORTUGUESE_PORTUGAL = "pt_PT"
    LOCALE_ROMANIAN = "ro"
    LOCALE_RUSSIAN = "ru"
    LOCALE_SERBIAN = "sr"
    LOCALE_SLOVAKIAN = "sk"
    LOCALE_SLOVENIAN = "sl"
    LOCALE_SPANISH = "es"
    LOCALE_SWEDISH = "sv"
    LOCALE_THAI = "th"
    LOCALE_TURKISH = "tr"
    LOCALE_UKRAINIAN = "uk"
    LOCALE_VIETNAMESE = "vi"

    # Known rules
    RULE_AVOID_BAD_REQUESTS = "AvoidBadRequests"
    RULE_AVOID_CHARSET_IN_META_TAG = "AvoidCharsetInMetaTag"
    RULE_AVOID_CSS_IMPORT = "AvoidCssImport"
    RULE_AVOID_EXCESS_SERIALIZATION = "AvoidExcessSerialization"
    RULE_AVOID_LONG_RUNNING_SCRIPTS = "AvoidLongRunningScripts"
    RULE_DEFER_PARSING_JAVASCRIPT = "DeferParsingJavaScript"
    RULE_ELIMINATE_UNNECESSARY_REFLOWS = "EliminateUnnecessaryReflows"
    RULE_ENABLE_GZIP_COMPRESSION = "EnableGzipCompression"
    RULE_INLINE_SMALL_CSS = "InlineSmallCss"
    RULE_INLINE_SMALL_JAVASCRIPT = "InlineSmallJavaScript"
    RULE_LEVERAGE_BROWSER_CACHING = "LeverageBrowserCaching"
    RULE_MAKE_LANDING_PAGE_REDIRECTS_CACHEABLE = \
        "MakeLandingPageRedirectsCacheable"
    RULE_MINIFY_CSS = "MinifyCss"
    RULE_MINIFY_HTML = "MinifyHTML"
    RULE_MINIFY_JAVASCRIPT = "MinifyJavaScript"
    RULE_MINIMIZE_REDIRECTS = "MinimizeRedirects"
    RULE_MINIMIZE_REQUEST_SIZE = "MinimizeRequestSize"
    RULE_OPTIMIZE_IMAGES = "OptimizeImages"
    RULE_OPTIMIZE_THE_ORDER_OF_STYLES_AND_SCRIPTS = \
        "OptimizeTheOrderOfStylesAndScripts"
    RULE_PREFER_ASYNC_RESOURCES = "PreferAsyncResources"
    RULE_PUT_CSS_IN_THE_DOCUMENT_HEAD = "PutCssInTheDocumentHead"
    RULE_REMOVE_QUERY_STRINGS_FROM_STATIC_RESOURCES = \
        "RemoveQueryStringsFromStaticResources"
    RULE_SERVE_RESOURCES_FROM_A_CONSISTENT_URL = \
        "ServeResourcesFromAConsistentUrl"
    RULE_SERVE_SCALED_IMAGES = "ServeScaledImages"
    RULE_SPECIFY_A_CACHE_VALIDATOR = "SpecifyACacheValidator"
    RULE_SPECIFY_A_VARY_ACCEPT_ENCODING_HEADER = \
        "SpecifyAVaryAcceptEncodingHeader"
    RULE_SPECIFY_CHARSET_EARLY = "SpecifyCharsetEarly"
    RULE_SPECIFY_IMAGE_DIMENSIONS = "SpecifyImageDimensions"
    RULE_SPRITE_IMAGES = "SpriteImages"

    # XXX: These rules are referenced on the PageSpeed Insights page, but
    # I haven't found their equivalent ids in any PageSpeed Insights analysis.
    # RULE_AVOID_CSS_EXPRESSIONS
    # RULE_MINIMIZE_DOCUMENT_WRITE
    # RULE_COMBINE_EXTERNAL_CSS
    # RULE_COMBINE_EXTERNAL_JAVASCRIPT
    # RULE_DEFER_LOADING_JAVASCRIPT
    # RULE_LEVERAGE_PROXY_CACHING
    # RULE_MINIMIZE_DNS_LOOKUPS
    # RULE_PARALLELIZE_DOWNLOADS_ACROSS_HOSTNAMES
    # RULE_REMOVE_UNUSED_CSS
    # RULE_SERVE_STATIC_CONTENT_FROM_A_COOKIELESS_DOMAIN
    # RULE_USE_EFFICIENT_CSS_SELECTORS

    # Supported strategies
    STRATEGY_DESKTOP = "desktop"
    STRATEGY_MOBILE = "mobile"

    __URL_DOMAIN = "www.googleapis.com"
    __URL_PATH = "/pagespeedonline/v1/runPagespeed"

    def __del__(self):

        """Destroys the Service object."""

        self.__key = None
        self.__user_ip = None

    def __init__(self, key, user_ip=None):

        """Constructs a new Service object.  The required key is the Google API
           key to use for all requests.  The optional 'user_ip' argument can be
           used to enforce per-user limits for usage of the API key."""

        self.__key = key
        self.__user_ip = user_ip

    def analyze(self, url, locale=LOCALE_ENGLISH_US, strategy=STRATEGY_DESKTOP,
                rules=None, connect_timeout=_GLOBAL_DEFAULT_TIMEOUT):

        """Makes a request to the Insights API to analyze the specified URL.
           The optional locale specifies the locale for the results (defaults
           to 'en_US').  The optional strategy specifies whether to analyze the
           page from a 'desktop' or 'mobile' perspective.  Use the optional
           'rules' argument to specify the list of rules to use in analysis (by
           default, all rules are run)."""

        # Construct URL
        query_data = {
            "key": [self.__key],
            "locale": [locale],
            "prettyprint": ["false"],
            "strategy": [strategy],
            "url": [url]
        }
        if rules is not None:
            query_data["rule"] = rules
        user_ip = self.__user_ip
        if user_ip is not None:
            query_data["userIp"] = [user_ip]
        path = "%s?%s" % (self.__URL_PATH, _urlencode(query_data, True))

        # Perform analysis
        conn = _HTTPSConnection(self.__URL_DOMAIN, timeout=connect_timeout)
        try:
            conn.request("GET", path)
            response = conn.getresponse()
            raw_data = response.read()
            status = response.status
        finally:
            conn.close()

        # Decode the response and handle the result
        data = _loads(raw_data)
        if status != 200:
            raise _Error(data)
        return _Analysis(data)
