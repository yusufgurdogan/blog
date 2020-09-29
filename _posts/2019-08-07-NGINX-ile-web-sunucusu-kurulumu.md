<!-- wp:paragraph -->
<p>Bu yazıda NGINX nedir, ne işe yarar, NGINX ile nasıl web sunucusu kurulur gibi sorular cevap bulacak.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"backgroundColor":"pale-cyan-blue"} -->
<p class="has-pale-cyan-blue-background-color has-background"><strong>Yazıyı okumadan önce bilinmesi gerekenler:</strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"backgroundColor":"very-light-gray","textColor":"vivid-cyan-blue"} -->
<p class="has-vivid-cyan-blue-color has-very-light-gray-background-color has-text-color has-background">NGINX yalnızca bir araçtır. Tek başına NGINX ile bir şey yapılmaz. NGINX'i web uygulamalarınızı çalıştırmak için kullanabilirsiniz.<br><a rel="noreferrer noopener" aria-label="Digitalocean'a üye olup
 (yeni sekmede açılır)" href="https://bit.ly/2ZJ32MW" target="_blank">Digitalocean'a üye olup</a> ayda 5 dolara Ubuntu işletim sistemi kurulu bir sunucu kiralayarak web uygulamalarınızı bu sunucu üzerinden 7/24 çalıştırabilirsiniz.<br>80 portu üzerinden sunarsanız  <em>(bu yazıda serve etmek yerine sunmak diyeceğim)</em> <strong>http://</strong> üzerinde, 443 portu ile sunarsanız <strong>https://</strong> üzerinde olur. <strong>https:/</strong>/ için SSL sertifikası almanız gerekir, bunu ücretli sunan servisler var ancak ücretsiz bir alternatif olan <a rel="noreferrer noopener" aria-label="LetsEncrypt (yeni sekmede açılır)" href="https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-18-04" target="_blank">LetsEncrypt</a> ile de SSL alabilirsiniz. Bu yazıda LetsEncrypt kullanacağız.<br>NGINX ayarlarında bir değişiklik yaptıktan sonra, ayarların doğru olup olmadığını test etmek için "<strong>nginx -t</strong>" komutuyla test edebilir, ayarları uygulamak için ise "<strong>systemctl reload nginx</strong>" komutunu kullanabilirsiniz.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>NGINX nedir?</strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>NGINX, yüksek performanslı bir HTTP sunucusu, ters (reverse) proxy ve aynı zamanda bir IMAP/POP3 proxy sunucusu olarak kullanılabilen bedava ve açık kaynaklı bir yazılımdır. Web sitelerinin birçoğunda; en çok bilinenlerinden Netflix, Airbnb, GitHub, SoundCloud gibi popüler sitelerde NGINX kullanılıyor.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>NGINX ne işe yarar?</strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>NGINX ile basit bir index.html dosyasını da sunabilirsiniz, halihazırda 4200 portunda çalışan bir Angular uygulamanız varsa buna reverse proxy kullanarak örneğin 80 portunda çalışmasını sağlayabilirsiniz, WordPress çalıştırabilirsiniz ve daha birçok şeyi sunabilirsiniz.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"align":"left"} -->
<h2 class="has-text-align-left">NGINX ile Statik Web Sitelerini Sunma Yöntemi</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Başlamadan önce 80 (ve HTTPS kullanacaksanız 443) portunuzun dışarıya açık olduğundan emin olun.</p>
<!-- /wp:paragraph -->

<!-- wp:preformatted -->
<pre class="wp-block-preformatted">sudo apt-get update
sudo apt-get install -y nginx</pre>
<!-- /wp:preformatted -->

<!-- wp:paragraph -->
<p>Nginx kurulumu tamamdır. Şimdi, sunucunuzun IP adresinizi tarayıcıya girerek kontrol edin, şu sayfayı gördüyseniz ilk adımı tamamladınız demektir:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":512} -->
<figure class="wp-block-image"><img src="https://yusufgurdogan.com/wp-content/uploads/2019/08/NGINX.png" alt="" class="wp-image-512"/><figcaption>Bu html dosyasınıın burada bulabilirsiniz:  "/var/www/html/index.nginx-debian.html"</figcaption></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Şimdi, Nginx'in kullandığı klasöre giderek kendimiz bir html dosyası oluşturalım, "index.html" ismini verelim ve nano adlı metin düzenleyicisi ile index.html dosyasını açalım.</p>
<!-- /wp:paragraph -->

<!-- wp:preformatted -->
<pre class="wp-block-preformatted">cd /var/www/html
nano index.html</pre>
<!-- /wp:preformatted -->

<!-- wp:paragraph -->
<p>Kendi HTML kodunuzu buraya sağ tıklayarak yapıştırın. HTML kodunuz yoksa deneme amaçlı olarak alttaki kodu kullanabilirsiniz:</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>&lt;!doctype html>
&lt;html>
  &lt;head>
    &lt;title>Deneme 1234&lt;/title>
  &lt;/head>
  &lt;body>
    &lt;p>Buraya metin gelecek.&lt;/p>
    &lt;marquee>:)&lt;/marquee>
  &lt;/body>
&lt;/html></code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>index.html dosyasını kaydedin: CTRL+X ve Y, ardından Enter. Tarayıcınızdan sayfayı yenileyin ve sayfanın değiştiğini göreceksiniz:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":515} -->
<div class="wp-block-image"><figure class="aligncenter"><img src="https://yusufgurdogan.com/wp-content/uploads/2019/08/NGINX-1.png" alt="" class="wp-image-515"/><figcaption>Sayfa değişmediyse şu komutu deneyin: <br><strong>systemctl reload nginx</strong></figcaption></figure></div>
<!-- /wp:image -->

<!-- wp:paragraph {"backgroundColor":"very-light-gray","textColor":"vivid-cyan-blue"} -->
<p class="has-vivid-cyan-blue-color has-very-light-gray-background-color has-text-color has-background">Evet, hepsi bu kadar. Basit bir HTML dosyasını sunmanız gerekiyorsa bu anlattıklarımı uygulamanız yeterlidir. Şimdi biraz ilerleyelim.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Elbette kullanıcılarınıza sitenize girmeleri için bir IP adresi vermeyeceksiniz. Bir domain aldıysanız, domaini sunucunuzun IP adresine yönlendirmeniz gerekir. Bu yönlendirme, domain sağlayıcınızın DNS ayarları üzerinden yapılabilir. Ben Namecheap kullanıyorum, domain ayarlarından "Advanced DNS" kısmına gelip buradan bir "A record" yani A kaydı oluşturacağım.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"textColor":"very-dark-gray","style":{"color":{"background":"#a7f0d3"}}} -->
<p class="has-very-dark-gray-color has-text-color has-background" style="background-color:#a7f0d3">Benim domain'im "yusufgurdogan.com" ve "deneme.yusufgurdogan.com" adresine (yani deneme subdomain'ine) bu IP adresini yönlendirmek istiyorum. DNS ayarlarından "Type" olarak A record'u seçtim, "Host" olarak "deneme" yazdım ve kaydettim. Birkaç dakika sonra, http://deneme.yusufgurdogan.com üzerinde yönlendirmenin tamamlandığını gördüm.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":518,"width":921,"height":159} -->
<figure class="wp-block-image is-resized"><img src="https://yusufgurdogan.com/wp-content/uploads/2019/08/DNS-1-1024x178.png" alt="" class="wp-image-518" width="921" height="159"/><figcaption>Bu şekilde kaydediyorum.</figcaption></figure>
<!-- /wp:image -->

<!-- wp:paragraph {"textColor":"very-dark-gray","style":{"color":{"background":"#a7f0d3"}}} -->
<p class="has-very-dark-gray-color has-text-color has-background" style="background-color:#a7f0d3">Eğer "yusufgurdogan.com" adresine yönlendirmek isteseydim, "deneme" yazdığım yere "@" yazıp kaydederdim. Bir de ekstradan "www" olarak da kaydederdim ki "www.yusufgurdogan.com" üzerinden de girilebilsin. Yani, şöyle olurdu:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":521,"width":892,"height":99} -->
<figure class="wp-block-image is-resized"><img src="https://yusufgurdogan.com/wp-content/uploads/2019/08/DNS-2-1024x114.png" alt="" class="wp-image-521" width="892" height="99"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph {"backgroundColor":"pale-cyan-blue"} -->
<p class="has-pale-cyan-blue-background-color has-background">Evet, şu ana kadar yaptıklarımızı bir özet geçelim:</p>
<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->
<ol><li>Nginx'i kurduk.</li><li>Kendi HTML sayfamızı web'e sunduk.</li><li>IP adresimizi domaine yönlendirdik.</li></ol>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>Bundan sonra ne yapalım? Bence bir SSL sertifikası alalım.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>HTTPS için her şeyden önce Nginx ayar dosyasından domaininizi belirtmeniz gerekiyor. Nginx ayar dosyasını açalım:</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>sudo nano /etc/nginx/sites-available/default</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>"server_name _;" bu ayarı değiştireceğiz. Benim domainim "deneme.yusufgurdogan.com"du, o yüzden bu ayarı şöyle değiştiriyorum:</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>server_name deneme.yusufgurdogan.com;</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>Siz kendi domaininizi yazın. CTRL+X ve Y, ardından Enter ile Nginx ayar dosyanızı kaydedin.</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>sudo add-apt-repository ppa:certbot/certbot</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>Yukarıdaki komutu girip Enter'layın. Certbot'un Nginx paketini kuralım:</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>sudo apt install -y python-certbot-nginx</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>Şimdi SSL sertifikasını alma zamanı:</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>sudo certbot --nginx -d deneme.yusufgurdogan.com -d www.deneme.yusufgurdogan.com</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>Size şimdi birkaç soru soracak. "Enter email address: " dediğinde mail adresinizi girin. SSL sertifikanızı yenilemeniz gerektiğinde ya da güvenlik açığı durumlarında size mail gönderirler. Ardından kullanım koşullarını kabul etmeniz gerekecek, "A" ve Enter. Ardından "Would you be willing to share your email address with the..." Yani diyor ki "ara sıra mail atsak sorun olur mu?" Ben istemediğim için "N" ile devam ettim. Bunun ardından "Please choose whether or not to redirect HTTP traffic to HTTPS, removing HTTP access." diyor ve "1: No redirect, 2: Redirect" seçeneklerini veriyor. 2 diyip devam etmenizi öneririm, http:// üzerinden giriş yapılırsa otomatik olarak https://'ye yönlendirmeye yarıyor. 1 ise yönlendirme yapmıyor.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"backgroundColor":"very-light-gray","textColor":"vivid-cyan-blue"} -->
<p class="has-vivid-cyan-blue-color has-very-light-gray-background-color has-text-color has-background">"Congratulations!" ile başlayan yazıyı gördüyseniz tamamdır. Sayfayı yenileyin ve siteye https:// ile, yani güvenli bir bağlantı ile girdiğinizi görün. Benim gördüğüm şudur:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":522,"width":490,"height":214} -->
<figure class="wp-block-image is-resized"><img src="https://yusufgurdogan.com/wp-content/uploads/2019/08/OK.png" alt="" class="wp-image-522" width="490" height="214"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Congratulations ile başlayan yazının devamında aslında önemli birkaç bilgi veriyor. Sertifika dosyalarının /etc/letsencrypt/live/.... klasöründe kaydedildiği bilgisi ve sertifikanızın ne zaman sona ereceği bilgisi önemli. Biz python-certbot-nginx ile kurduğumuz için otomatik sertifika yenilemelerini /etc/cron.d klasöründe kendisi ayarladı. Yine de aklınızda bulunsun, manuel olarak sertifikayı yenilemeniz gerekirse <code>certbot renew</code> komutunu kullanabilirsiniz.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"backgroundColor":"very-light-gray","textColor":"vivid-cyan-blue"} -->
<p class="has-vivid-cyan-blue-color has-very-light-gray-background-color has-text-color has-background">Not: Yukarıda bahsettiğim yönlendirme olayında 2'yi seçtiyseniz, http'yi https'ye yönlendirmesi gerekir. Bunu test etmek için tarayıcınızdan aynı adrese "http://" kullanarak girmeyi deneyin. https'ye yönlendiriyorsa, testi geçtiniz demektir.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>NGINX ile Reverse Proxy Nasıl Yapılır?</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Statik dosyaların nasıl sunulacağını gördük. Şimdi, sunucunuzda halihazırda bir port üzerinde sunulan bir servisi reverse proxy ile nasıl NGINX ile sunabiliriz onu görelim. Bir Angular uygulamanız var diyelim, localhost'ta 4200 portu üzerinde çalışıyor. Bunu example.com domaininin 80 portuna yönlendirmek istiyorsunuz. Aşağıdaki blok ile bu yönlendirmeyi yapabilirsiniz:</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>server {
    listen 80;
    server_name example.com; # kendi domaininizi girin
    location / {
        proxy_pass http://localhost:4200;
        proxy_set_header Host $host;
    }
}</code></pre>
<!-- /wp:code -->

<!-- wp:heading -->
<h2>NGINX ve Server Blokları</h2>
<!-- /wp:heading -->

<!-- wp:paragraph {"textColor":"very-dark-gray","style":{"color":{"background":"#b8e7d5"}}} -->
<p class="has-very-dark-gray-color has-text-color has-background" style="background-color:#b8e7d5">"/etc/nginx/sites-available/default" dosyasında, Nginx'e her bir server bloğunda istediğiniz domaini (ya da subdomaini) sunabilirsiniz. Üstelik, bunu aynı portlar üzerinden yapsanız da bir çakışma olmaz. Örneğin, 80 ve 443 portunu kullanan 3 ayrı projenizi farklı domainlere yönlendirerek aynı sunucu üzerinden çalıştırabilirsiniz. Bunu yapmak için ekstradan 2 sunucu alıp onlara Nginx kurmanıza gerek yoktur.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Server bloklarının içinde, hangi web sayfasının nereye gideceğini de belirleyebilirsiniz. Örnek bir ayar dosyası yapalım. /login/ sayfasına giren birisi, sizin oluşturduğunuz /var/www/html/test/ klasörüne gitsin. Olmayan bir sayfaya gitmeye çalışan kullanıcı /spool/www konumundaki 404.html sayfasına gitsin. Bu ayarları, ayar dosyasına şöyle yazabiliriz:</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>location = /login/ {
    root /var/www/html/test;
}

error_page  404  /404.html;

location = /404.html {
    root  /spool/www;
}</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>Server bloklarında daha neler yapılabilir sorusunun cevabı için aşağıdaki bağlantıları ziyaret edebilirsiniz:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li><a rel="noreferrer noopener" aria-label=" (yeni sekmede açılır)" href="https://www.nginx.com/resources/wiki/start/topics/examples/server_blocks/" target="_blank">https://www.nginx.com/resources/wiki/start/topics/examples/server_blocks/</a></li><li><a rel="noreferrer noopener" aria-label=" (yeni sekmede açılır)" href="https://www.linode.com/docs/web-servers/nginx/how-to-configure-nginx/#server-blocks" target="_blank">https://www.linode.com/docs/web-servers/nginx/how-to-configure-nginx/#server-blocks</a></li></ul>
<!-- /wp:list -->

<!-- wp:heading -->
<h2>NGINX ile Load Balancing (Yük Dengeleme) Nasıl Yapılır?</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Yük dengeleme sayesinde sunucunuza gelen trafiği diğer sunucularınıza yönlendirebilirsiniz. Diyelim ki 3 adet sunucunuz var ve tüm yük birinde toplansın istemiyorsunuz, bu yükü üçüne dağıtmak istiyorsunuz. Ana sunucu üzerinden şöyle bir ayar yapabilirsiniz:</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>upstream backend {
 server localhost:1234; # ana sunucu
 server 18.131.154.122; # yedek 1
 server 85.94.218.43 # yedek 2
}
server {
    listen 80;
    server_name example.com; # kendi domaininizi girin
    location / {
        proxy_pass       http://backend;
        proxy_set_header Host            $host;
    }
}</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>Yük dengeleme hakkında detaylı bilgi için aşağıdaki adresleri ziyaret edebilirsiniz:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li><a href="http://nginx.org/en/docs/http/load_balancing.html">http://nginx.org/en/docs/http/load_balancing.html</a></li><li><a href="https://upcloud.com/community/tutorials/configure-load-balancing-nginx/">https://upcloud.com/community/tutorials/configure-load-balancing-nginx/</a></li><li><a href="https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-load-balancing">https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-load-balancing</a></li></ul>
<!-- /wp:list -->

<!-- wp:heading -->
<h2 id="Direkt-IP">Direkt IP Üzerinden Erişimi Yönetme &amp; Engelleme</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Yaptığınız web sitesine yalnızca domain üzerinden erişilebilmesini istiyorsunuz. Birisi IP adresinizi bulursa ve oradan erişmeye çalışırsa ne olacak? Hiçbir ayar yapmazsanız, varsayılan olarak "Welcome to NGINX" sayfası çıkar. NGINX ile bu sayfayı kapatabilirsiniz ya da domain'e yönlendirebilirsiniz.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Aşağıdaki örneklerde, sunucumuzun IP adresi 3.78.104.56 ve domainimiz example.com.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>IP adresinden erişmeye çalışan birisi domain'e yönlensin istiyorsanız kullanmanız gereken server bloğu:</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>server {
    server_name 3.78.104.56;
    return 301 http://example.com;
}</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>IP adresinden erişmeye çalışan birisi 404 hatası alsın istiyorsanız kullanmanız gereken server bloğu:</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>server {
    server_name 3.78.104.56;
    return 404;
}</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>IP adresinden erişmeye çalışan birisi sunucuya <strong>bağlanamasın</strong> istiyorsanız:</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>server {
    server_name 3.78.104.56;
    return 0;
}</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>Ayarları uygulamak için <strong>systemctl reload nginx</strong> komutunu kullanabilirsiniz.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>NGINX Nasıl Kaldırılır?</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>NGINX'i ayar dosyaları hariç olarak kaldırmak için:</p>
<!-- /wp:paragraph -->

<!-- wp:preformatted -->
<pre class="wp-block-preformatted">sudo apt-get remove nginx nginx-common
sudo apt-get autoremove </pre>
<!-- /wp:preformatted -->

<!-- wp:paragraph -->
<p>NGINX'i tamamen kaldırmak için:</p>
<!-- /wp:paragraph -->

<!-- wp:preformatted -->
<pre class="wp-block-preformatted">sudo apt-get purge nginx nginx-common<br>sudo apt-get autoremove  </pre>
<!-- /wp:preformatted -->

<!-- wp:paragraph -->
<p>Yararlanılan kaynaklar:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li><a rel="noreferrer noopener" aria-label="https://www.nginx.com/resources/wiki/ 
 (yeni sekmede açılır)" href="https://www.nginx.com/resources/wiki/" target="_blank">https://www.nginx.com/resources/wiki/</a></li><li><a rel="noreferrer noopener" aria-label=" (yeni sekmede açılır)" href="http://nginx.org/en/docs/example.html" target="_blank">http://nginx.org/en/docs/example.html</a></li><li><a rel="noreferrer noopener" aria-label="https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-18-04  (yeni sekmede açılır)" href="https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-18-04" target="_blank">https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-18-04</a></li><li><a href="https://askubuntu.com/a/235349/908691">https://askubuntu.com/a/235349/908691</a></li></ul>
<!-- /wp:list -->