import pandas as pd
from psinsights import Service

# my Google API key
service = Service('AIzaSyA3FfXgcx1LF5wLNUjVrFB9ioJ8cQrRgkM')
# list of URLs
url = ['https://www.gov.uk/government/news/right-to-rent-checks-what-they-mean-for-you', 'https://www.gov.uk/government/publications/rules-and-acceptable-documents-right-to-rent-checks']
# define dataframe
headings = ['URL', 'Title', 'PageSpeed score', 'Total Resource count', 'Total Request Bytes', 'Static Resource count', 'CSS Resource count', 'CSS Response Bytes', 'Flash Response Bytes', 'Host Count', 'HTML Response Bytes', 'Image Response Bytes', 'JavaScript Resource Count', 'JavaScript Response Bytes', 'Text Response Bytes', 'Other Response Bytes']
table = []
speed = pd.DataFrame(columns=headings, data=table)

# loop through each url
for page in url:
    analysis = service.analyze(page)
    stats = analysis.statistics
    # get data into list
    newrow = [page, analysis.title, analysis.score, stats.resource_count,
     stats.total_request_bytes, stats.static_resource_count,
     stats.css_resource_count, stats.css_response_bytes,
     stats.flash_response_bytes, stats.host_count,
     stats.html_response_bytes, stats.image_response_bytes,
     stats.javascript_resource_count,
     stats.javascript_response_bytes, stats.text_response_bytes,
     stats.other_response_bytes]
    # turn data list  into dataframe
    newrowdf = pd.Series(newrow, index=headings)
    # append dataframe to main dataframe
    speed = speed.append(newrowdf, ignore_index=True)

print speed