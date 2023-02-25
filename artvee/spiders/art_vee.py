import scrapy
import pandas as pd

class ArtVeeSpider(scrapy.Spider):
    name = "art_vee"
    classic = [
    {'type': 'classical_art', 'category': 'Abstract', 'link': 'https://artvee.com/c/abstract/'},
    {'type': 'classical_art', 'category': 'Figurative', 'link': 'https://artvee.com/c/figurative/'},
    {'type': 'classical_art', 'category': 'Landscape', 'link': 'https://artvee.com/c/landscape/'},
    {'type': 'classical_art', 'category': 'Religion', 'link': 'https://artvee.com/c/religion/'},
    {'type': 'classical_art', 'category': 'Mythology', 'link': 'https://artvee.com/c/mythology/'},
    {'type': 'classical_art', 'category': 'Posters', 'link': 'https://artvee.com/c/posters/'},
    {'type': 'classical_art', 'category': 'Drawings', 'link': 'https://artvee.com/c/drawings/'},
    {'type': 'classical_art', 'category': 'Illustration', 'link': 'https://artvee.com/c/illustration/'},
    {'type': 'classical_art', 'category': 'Still Life', 'link': 'https://artvee.com/c/still-life/'},
    {'type': 'classical_art', 'category': 'Animals', 'link': 'https://artvee.com/c/animals/'},
    {'type': 'classical_art', 'category': 'Botanical', 'link': 'https://artvee.com/c/botanical/'},
    {'type': 'classical_art', 'category': 'Asian Art', 'link': 'https://artvee.com/c/asian-art/'},
    {'type': 'modern_art', 'category': 'Abstract', 'link': 'https://artvee.com/c/modern-art/abstract-modern-art/'},
    {'type': 'modern_art', 'category': 'Figurative', 'link': 'https://artvee.com/c/modern-art/figurative-modern-art/'},
    {'type': 'modern_art', 'category': 'Illustration', 'link': 'https://artvee.com/c/modern-art/illustration-modern-art/'},
    {'type': 'modern_art', 'category': 'Surrealism', 'link': 'https://artvee.com/c/modern-art/surrealism/'},
    {'type': 'modern_art', 'category': 'Posters', 'link': 'https://artvee.com/c/modern-art/posters-modern-art/'},
    {'type': 'modern_art', 'category': 'Drawings', 'link': 'https://artvee.com/c/modern-art/drawings-modern-art/'},
    {'type': 'modern_art', 'category': 'Pop Art', 'link': 'https://artvee.com/c/modern-art/pop-art/'},
    {'type': 'modern_art', 'category': 'Still Life', 'link': 'https://artvee.com/c/modern-art/still-life-modern-art/'},
    {'type': 'modern_art', 'category': 'Landscape', 'link': 'https://artvee.com/c/modern-art/landscape-modern-art/'},
    {'type': 'modern_art', 'category': 'Animals', 'link': 'https://artvee.com/c/modern-art/animals-modern-art/'},
    {'type': 'modern_art', 'category': 'Expressionism', 'link': 'https://artvee.com/c/modern-art/expressionism/'},
    {'type': 'modern_art', 'category': 'Pop Surrealism', 'link': 'https://artvee.com/c/modern-art/pop-surrealism/'}
    ]
    def start_requests(self):
        for url in self.classic:
            d_type = url['type']
            category = url['category']
            link = url['link']
            per_page_70 = '?per_page=70'
            link_70 = f'{link}{per_page_70}'
            if category == 'Botanical':
                file_name = f'{category}.xlsx'
                df = pd.DataFrame()
                df.to_excel(file_name, index=False)
                yield scrapy.Request(url=link_70, callback=self.parse, meta={'d_type':d_type, 'category': category, 'file_name': file_name})
    
    def parse(self, response):
        content = response.css('h3.product-title')
        d_type = response.meta.get('d_type')
        category = response.meta.get('category')
        file_name = response.meta.get('file_name')
        df = pd.read_excel(file_name)
        for c in content:
            title_en = c.css('a::text').get()
            title = title_en
            link = c.css('a::attr(href)').get()
            data = {'type':d_type, 'category':category, 'title': title, 'link': link}
            df = df.append([data])
            yield  data
            
        
        df.to_excel(file_name, index=False)
        
        next_page = response.css('ul.page-numbers li a.next::attr(href)').get()
        if next_page is not None:
            yield scrapy.Request(url= next_page, callback=self.parse, meta={'d_type':d_type, 'category': category, 'file_name': file_name})

