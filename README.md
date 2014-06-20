Scrapy project for http://store.steampowered.com/ 
=============================

A scrapy project to retrieve game infos on http://store.steampowered.com/

[![PayPayl donate button](http://img.shields.io/paypal/donate.png?color=yellow)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=BR744DG33RAGN "Make a donate")

<script data-button="donate" src="https://www.paypalobjects.com/js/external/paypal-button.min.js?merchant=YT8HJ754TNAVL"></script>

# Extracted Fields
This scrapy project capable to extract the following fields from the website:
```
name
poster
video
video_hd
genres
developer
publisher
release_date
languages
about
website
warning
requirements
    mac
        minimum
            os
            processor
            memory
        recommended
            os
            processor
            memory
    pc
        minimum
            os
            processor
            memory
            directx
            hard_drive
            network
        recommended
            os
            processor
            memory
            directx
            hard_drive
            network
```
# Execute
```
scrapy crawl steampowered_com
```

# Execute and Export to CSV
```
scrapy crawl steampowered_com -o steampowered_com.csv -t csv
```
