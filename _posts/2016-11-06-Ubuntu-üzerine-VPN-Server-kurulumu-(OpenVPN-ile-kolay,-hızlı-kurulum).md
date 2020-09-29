Ubuntu üzerine OpenVPN server kuracağız ve çok basit olacak.

Digitalocean anlatımlarında&nbsp;<a href="https://www.digitalocean.com/community/tutorials/how-to-set-up-an-openvpn-server-on-ubuntu-14-04" target="_blank" rel="noopener noreferrer">(Ubuntu 14.04 için OpenVPN kurulumu)</a> <a href="https://www.digitalocean.com/community/tutorials/how-to-set-up-an-openvpn-server-on-ubuntu-16-04" target="_blank" rel="noopener noreferrer">(Ubuntu 16.04 için OpenVPN kurulumu)</a>&nbsp;her şeyi adım adım anlatıyor. Biz uzun anlatımda yapılan birçok şeyi kendiliğinden yapacak bir sh dosyası kullanacağız. Haydi başlayalım!
<ol>
 	<li style="list-style-type: none;">
<ul>
 	<li>Ubuntu server'ınıza root olarak giriş yapın. Ben <a href="http://www.putty.org/" target="_blank" rel="noopener noreferrer">putty</a> kullanıyorum.
<a href="/blog/assets/images/ubuntu-login.png" target="_blank" rel="noopener noreferrer"><img class="alignnone wp-image-142 size-full" src="/blog/assets/images/ubuntu-login.png" alt="ubuntu-login" width="661" height="466"></a></li>
 	<li>Klasik başlangıç: <span style="color: #0000ff;">root yetkileri verilir</span> (her seferinde&nbsp;sudo yazmamak için) ve <span style="color: #ff0000;">update yapılır</span>.</li>
 	<li>
<pre><span style="color: #0000ff;"><code>sudo -s</code></span></pre>
</li>
 	<li>
<pre><code></code><span style="color: #ff0000;">apt-get update</span></pre>
</li>
</ul>
</li>
</ol>
<ul>
 	<li>Bu komutu yazıp enterlayın:</li>
 	<li>
<pre><code class="shell plain">cat /dev/net/tun
</code></pre>
</li>
</ul>
<a href="/blog/assets/images/ubuntu-file-descriptor-in-bad-state.png" target="_blank" rel="noopener noreferrer"><img class=" wp-image-151 size-full alignleft" src="/blog/assets/images/ubuntu-file-descriptor-in-bad-state.png" alt="" width="385" height="51"></a>&nbsp;Böyle yazması gerekiyor. Hata gibi görünüyor, değil mi?<strong>&nbsp;Böyle yazıyorsa sorun yok demektir, diğer adıma geçebilirsiniz.</strong> Böyle yazmıyorsa, server'ınızda&nbsp;TUN/TAP özelliği açık değil demektir. VPS'niz&nbsp;OpenVZ&nbsp;üzerine ise ve VPS manager'ı&nbsp;SolusVM ise&nbsp;SolusVM'de bu seçeneği görebilirsiniz. "On" yapın.<a href="/blog/assets/images/vpn-enable-tun-tap.png"><img class="alignnone wp-image-148 size-full" src="/blog/assets/images/vpn-enable-tun-tap.png" alt="vpn-enable-tun-tap" width="498" height="227"></a>
<ul>
 	<li>Şimdi OpenVPN kuruluma bu sihirli satırla başlıyoruz:</li>
</ul>
<ul>
 	<li style="list-style-type: none;">
<ul>
 	<li>
<pre><code class="shell plain">wget git.io/vpn --no-check-certificate -O openvpn-install.sh; bash openvpn-install.sh</code></pre>
</li>
</ul>
</li>
</ul>
<a href="https://github.com/Nyr/openvpn-install/blob/master/openvpn-install.sh" target="_blank" rel="noopener noreferrer">openvpn-install.sh dosyasını GitHub'da incelemek isterseniz tıklayın.</a>

Bundan sonra 1-2 dakika kadar bir işlem yapabilir. Ondan sonra&nbsp;<strong>(daha önce OpenVPN kurduysanız)</strong> şöyle bir soru soracak size:
<a href="/blog/assets/images/openvpn-already-installed.png"><img class="alignleft wp-image-153 size-full" src="/blog/assets/images/openvpn-already-installed.png" alt="openvpn-already-installed" width="320" height="166"></a>"OpenVPN kurulmuş, ne yapalım?" Öncekini kaldırmanızı&nbsp;öneriyorum ben, "<span style="text-decoration: underline;"><strong>3" e basıp enterlayın, sonra da "y" , enter.</strong></span>

3'ü seçip kaldırmıştık, şimdi tekrar yüklemek için aynı komutu yine gireceğiz:

 	<li>
<pre><code class="shell plain">wget git.io/vpn --no-check-certificate -O openvpn-install.sh; bash openvpn-install.sh</code></pre>
</li>
</ul>
</li>
</ul>
<strong>
"IP Address:"</strong> karşısındakini silip VPS'nizin IP adresini yazın. Benimki&nbsp;13.81.167.131 gibi bir adres.
<strong>"Which protocol do you want for OpenVPN connections?"</strong> OpenVPN için hangi protokolü kullanmak istediğinizi soruyor. UDP olsun: 1 ve enter.
<strong>"What port do you want OpenVPN listening to:"</strong> karşısında 1194 yazıyor, isterseniz 443 olarak ya da istediğiniz bir portla değiştirebilirsiniz.
<strong>"What DNS do you want to use with the&nbsp;VPN?"&nbsp;</strong>yani diyor ki, bu VPN ile hangi DNS'i kullanmak istiyorsun? Ben Google DNS'ini kullanıyorum, size de öneririm.<strong>
"Client name:"</strong>&nbsp;"client" olarak kalabilir, enterlayın geçin.

Tekrar enterladıktan sonra kurulumu yaparken sizi birkaç dakika bekletecek.
<ul>
 	<li>VPN kurulumu tamamdır. :) Şimdi karşınızdaki ekranda ne yazıyor onları anlatayım biraz.
<a href="/blog/assets/images/client-ovpn.png">
</a><a href="/blog/assets/images/client-ovpn.png"><img class="alignnone wp-image-154" src="/blog/assets/images/client-ovpn.png" alt="client-ovpn" width="650" height="411"></a><em>Üstte diyor ki, sertifika 3650 gün (10 yıl) boyunca geçerlidir... Bunları geçelim</em>, altta bize lazım olan şey yazıyor:
<strong>Your client config is available at ~/client.ovpn</strong>
<em>Client config'iniz&nbsp;~/client.ovpn'de hazır.</em><strong> Şimdi bu dosyayı kendi bilgisayarınıza indirmeniz gerek ki VPN bağlantısı yapabilesiniz.</strong> İndirdikten sonra ister ios, ister android, ister windows bilgisayarınızda kullanabileceksiniz.
<strong>Bu dosyayı ubuntu sunucumdan kendi bilgisayarıma indirebilmek için&nbsp;Windows PowerShell kullanacağım. Dosyayı "karşıdan yüklemeniz" gerekmiyorsa yani dosya başka bir sunucuda değilse bu adımları geçebilirsiniz.</strong></li>
</ul>
<ol>
 	<li>Başlat menüsünde Powershell yazarak Windows Powershell'i açın.</li>
 	<li>
<blockquote>pscp.exe kullaniciadi@IPadresi:client.ovpn C:\Users\KullaniciAdiniz\Desktop\client.ovpn</blockquote>
Burada kullaniciadi yerine sunucuza bağlanırken kullandığınız kullanıcı adınızı, IPadresi yerine sunucunuzun IP adresini, client.opvn yerine başka bir şey yazdıysanız onu değiştirin, KullaniciAdiniz yerine bilgisayarınızda oturum açmış olduğunuz kullanıcı adını <em>(bilmiyorsanız C:\Users yolunu izleyin, orada kullanıcı adınız görünecektir.)</em> yazın ve bu düzenlenmiş halini satırı PowerShell'e yapıştırın.</li>
 	<li>Sunucunuzun şifresini isteyecektir, girip enterlayın.</li>
 	<li>"client.ovpn&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;| 8 kB |&nbsp; &nbsp;8.0 kB/s | ETA: 00:00:00 | 100%" yazıyorsa tamamdır, client.ovpn dosyası bilgisayarınızda masaüstüne kaydedilmiş demektir.</li>
</ol>
Şimdi OpenVPN indireceğiz ve client.ovpn dosyasını kullanacağız. Android ve iOS'a da indirebilirsiniz, ben Windows için anlatmaya devam ediyorum.
<ol>
 	<li><a href="https://openvpn.net/index.php/open-source/downloads.html" target="_blank" rel="noopener noreferrer">OpenVPN client'ini indirin</a>.</li>
 	<li>client.ovpn dosyanızı "C:\Program Files\OpenVPN\config" buraya atın.</li>
 	<li>OpenVPN client'ini açın. Sonrası resimde.<a href="/blog/assets/images/openvpn-gui1.png"><img class="alignnone wp-image-169 size-full" src="/blog/assets/images/openvpn-gui1.png" alt="" width="554" height="287"></a></li>
 	<li>Bu kadar. VPN'e bağlı olduğunuza emin olmak için <a href="https://www.iplocation.net/find-ip-address">buradan</a> IP adresinizi ve IP adresinin lokasyonuna bakabilirsiniz.</li>
 	<li>Bundan sonra bir hata alırsanız, openvpn simgesine sağ tıklayıp resimdeki "Günlüğe Bak"a tıklayın ve çıkan metin belgesindeki son satırları Google'da aratın. Ben de çok hatayla karşılaştım, neyse ki Google'da araştırarak çözüme ulaştım.
Bağlantı sorunu yaşıyorsanız "1194" portunu açmamış olabilirsiniz (azure, google cloud vs. için geçerli bu). Sunucunun sağlayıcısından&nbsp;destek alabilirsiniz.</li>
</ol>
<h2>VPN kurulumunda sık karşılaşılan hataların çözümleri</h2>
<ul>
 	<li>
<h4><strong>MANAGEMENT: &gt;STATE:1524301594,WAIT,,,</strong> 'te kalıyor, VPN'e bağlanmıyor.</h4>
Olası çözümler:</li>
</ul>
<ol>
 	<li>Portlar dışarıdan kapalı olabilir. Dışarıdan dediğim, örneğin Microsoft Azure ile açtıysanız Azure panelinden portu açmanız gerekir. (Settings -&gt; Networking yolunu izledikten sonra Inbound ve Outbound Port kurallarından 1194'e ya da seçtiğiniz porta izin vermelisiniz.</li>
 	<li>Portlar içerinden kapalı olabilir. Yani, ufw kullanarak&nbsp;bazı izinler vermelisiniz.
<ol>
 	<li><span style="text-decoration: underline;">sudo -s</span>&nbsp;ile root yetkilerini alın.</li>
 	<li><span style="text-decoration: underline;">ufw enable</span>&nbsp;ile ufw'yi aktifleştirin, "y", enter.</li>
 	<li><span style="text-decoration: underline;">ufw allow 1194/udp ile 1194 portunu UDP olarak açın.</span></li>
 	<li><span style="text-decoration: underline;">ufw allow OpenSSH</span> ile SSH portuna da izin verin.</li>
 	<li><span style="text-decoration: underline;">ufw status</span> ile açtığınız portlara göz atabilirsiniz.</li>
 	<li>Tekrar bağlanmayı deneyin.</li>
</ol>
</li>
</ol>
<ul>
 	<li><strong>VPN'e bağlanıyor ama internet erişimi yok. Yani VPN üzerinden internete bağlanmıyor.</strong></li>
</ul>
<ol>
 	<li><span style="text-decoration: underline;">sysctl net.ipv4.ip_forward=1</span></li>
 	<li><span style="text-decoration: underline;">iptables -I FORWARD -j ACCEPT</span></li>
 	<li><span style="text-decoration: underline;">iptables -t nat -I POSTROUTING -s 10.8.0.0/24 -o eth0 -j MASQUERADE</span></li>
 	<li>Bağlanmayı tekrar deneyin.</li>
</ol>
<ul>
 	<li>Android'e, iOS'a nasıl kuracağız bu VPN'i, Mac'te VPN nasıl kullanacağız ... sorularının cevabı <a href="https://www.digitalocean.com/community/tutorials/how-to-set-up-an-openvpn-server-on-ubuntu-14-04#step-5-installing-the-client-profile" target="_blank" rel="noopener noreferrer">burada</a>. Bu client.ovpn dosyasında VPN'in kullanıcı adı, sertifika gibi bilgiler var. O dosyaya sahip olan VPN'e rahatlıkla bağlanabilir bunu unutmayın.</li>
 	<li>VPN gerçekten işe yarıyor. VPN sağlayıcılarının IP aralıkları engellense dahi siz etkilenmeyeceksiniz çünkü VPN sağlayıcısından almadınız, kendi VPN'inizi kendiniz kurdunuz. Çok havalı değil mi? :)</li>
</ul>
