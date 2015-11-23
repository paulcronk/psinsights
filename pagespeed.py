import pandas as pd
from psinsights import Service
from sys import stdout

# My Google API key
service = Service('AIzaSyA3FfXgcx1LF5wLNUjVrFB9ioJ8cQrRgkM')
# list of URLs
url = ['https://www.gov.uk/government/news/right-to-rent-checks-what-they-mean-for-you', 'https://www.gov.uk/government/publications/rules-and-acceptable-documents-right-to-rent-checks']
# define dataframe
headings = ['URL', 'Title', 'PageSpeed score', 'Total Resource count', 'Total Request Bytes', 'Static Resource count', 'CSS Resource count', 'CSS Response Bytes', 'Flash Response Bytes', 'Host Count', 'HTML Response Bytes', 'Image Response Bytes', 'JavaScript Resource Count', 'JavaScript Response Bytes', 'Text Response Bytes', 'Other Response Bytes']
table = []
speed = pd.DataFrame(columns=headings, data=table)
# print speed.head()

for page in url:
    analysis = service.analyze(page)
    stats = analysis.statistics

    newrow = [page, analysis.title, analysis.score, stats.resource_count,
     stats.total_request_bytes, stats.static_resource_count,
     stats.css_resource_count, stats.css_response_bytes,
     stats.flash_response_bytes, stats.host_count,
     stats.html_response_bytes, stats.image_response_bytes,
     stats.javascript_resource_count,
     stats.javascript_response_bytes, stats.text_response_bytes,
     stats.other_response_bytes]

    print newrow

    newrowdf = pd.DataFrame(columns=headings, data=newrow)
    print newrowdf
    speed = speed.append(newrowdf,ignore_index=True)

# print speed

#    stdout.write("URL: %s\n"
#                 "Title: %s\n"
#                 "Google PageSpeed score: %s\n"
#                 "Total Resource count: %s\n" # Number of HTTP resources loaded by the page
#                 "Total Request Bytes: %s\n" # Total size of all request bytes sent by the page.
#                 "Static Resource count: %s\n" # Number of static (i.e. cacheable) resources on the page.
#                 "CSS Resource count: %s\n" # Number of CSS resources referenced by the page.
#                 "CSS Response Bytes: %s\n" # Number of uncompressed response bytes for CSS resources on the page.
#                 "Flash Response Bytes: %s\n" # Number of response bytes for flash resources on the page.
#                 "Host Count: %s\n" # Number of unique hosts referenced by the page.
#                 "HTML Response Bytes: %s\n" # Number of uncompressed response bytes for the main HTML document and all iframes on the page.
#                 "Image Response Bytes: %s\n" # Number of response bytes for image resources on the page.
#                 "JavaScript Resource Count: %s\n" # Number of JavaScript resources referenced by the page.
#                 "JavaScript Response Bytes: %s\n" # Number of uncompressed response bytes for JS resources on the page.
#                 "Text Response Bytes: %s\n" # Number of uncompressed response bytes for text resources not covered by other statistics (i.e non-HTML, non-script, non-CSS resources) on the page.
#                 "Other Response Bytes: %s\n" % # Number of response bytes for other resources on the page.
#                 (page, analysis.title, analysis.score, stats.resource_count,
#                  stats.total_request_bytes, stats.static_resource_count,
#                  stats.css_resource_count, stats.css_response_bytes,
#                  stats.flash_response_bytes, stats.host_count,
#                  stats.html_response_bytes, stats.image_response_bytes,
#                  stats.javascript_resource_count,
#                  stats.javascript_response_bytes, stats.text_response_bytes,
#                  stats.other_response_bytes))
