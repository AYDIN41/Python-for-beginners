import scrapy


class BooksSpider(scrapy.Spider):
    name = "computer"
    page_count = 0
    book_count = 1
    dosya = open("books.txt","a",encoding="UTF-8")
    start_urls = [
        "https://www.trendyol.com/sr?q=laptop&qt=laptop&st=laptop&os=1"
    ]

    def parse(self, response):
        computer_names = response.css("div.prdct-desc-cntnr div.prdct-desc-cntnr-ttl-w.two-line-text span.prdct-desc-cntnr-ttl::text").extract()
        computer_features = response.css("div.prdct-desc-cntnr div.prdct-desc-cntnr-ttl-w.two-line-text  span.prdct-desc-cntnr-name.hasRatings::text").extract()
        

        i = 0
        while (i < 10):
            """yield {
                "name" : book_names[i],
                "author" : book_authors[i],
                "publisher" : book_publishers[i]
            }"""
            self.dosya.write("***************************-***************\n")
            self.dosya.write(str(self.book_count) + ".kitap : " + computer_names[i])
            self.dosya.write("\n Yazar : " + computer_features[i])
            
           
            self.book_count += 1
            i += 1
        