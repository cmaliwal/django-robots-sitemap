There are basically three steps that are involved in the web crawling procedure. First, the search bot starts by crawling the pages of your site. Then it continues indexing the words and content of the site, and finally it visit the links (web page addresses or URLs) that are found in your site. When the spider doesn’t find a page, it will eventually be deleted from the index. However, some of the spiders will check again for a second time to verify that the page really is offline.

The first thing a spider is supposed to do when it visits your website is look for a file called “robots.txt”. This file contains instructions for the spider on which parts of the website to index, and which parts to ignore. The only way to control what a spider sees on your site is by using a robots.txt file. All spiders are supposed to follow some rules, and the major search engines do follow these rules for the most part. Fortunately, the major search engines like Google or Bing are finally working together on standards.
 
Robots.txt file : Robots.txt is basically a text file that defines the rules of search engine robots (bot) to inform the robots  what part of the website should be indexed  and what urls should not be indexed.
 
Example :
User-agent: *
Disallow: /sot-admin/
Disallow: /404.html?page=
Disallow: *&search=s
Disallow: */tag/
Disallow: */?page_id=
Sitemap: http://sayonetech.com/sitemap.xml
For more details about robots.txt file : http://www.robotstxt.org/robotstxt.html
 
Sitemap.xml : Sitemap is very important piece of information for any website which help  search engines to index  your website.
 
Its simple xml file having information about all the urls of our website with priority, change frequency and other parameter as  well.THis help search engine to learn about the site’s   structure and index our website.
 
The sitemap framework : 
Django comes with a high level sitemap-generating framework that makes creating sitemap xml file  easy.
For more details : https://docs.djangoproject.com/en/2.0/ref/contrib/sitemaps/
 
One more important things is to let google knows about changes in our sitemap.xml  so that our site can be re-indexed.
The sitemap framework provides a function just to do that :
django.contrib.sitemaps.ping_google()
Note : Make sure  to register your site with google webmaster tools otherwise this commands will not work.
 
Take reference : http://nanvel.name/2013/07/sitemap-and-robots
