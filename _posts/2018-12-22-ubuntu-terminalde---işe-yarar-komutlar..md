<h2><span style="color: #33cccc;">başlangıç (1/3)</span></h2>
dosya kopyalama, bir klasöre gitme, dosya silme gibi ufak tefek şeyler. sırasıyla yapabilirsiniz.

- bulunduğum klasörde neler var, nasıl görebilirim?
<code><span class="lit">ls</span></code>
- ana klasöre gitmek istiyorum.
<code><span class="lit">cd ~/</span></code>
<em>(ya da yalnızca&nbsp;</em><code><span class="lit">cd</span></code><em>)</em>
- bir klasör oluşturmak istiyorum. ismi folder olsun.
<code><span class="lit">mkdir folder</span></code>
- bulunduğum klasöre metin.txt diye bir metin belgesi açıp bir şeyler yazmak istiyorum.
<code><span class="lit">nano metin.txt</span></code>
<em>bir şeyler yazın.</em>
<em>kaydetmek için sırasıyla:</em> ctrl+x, y, enter
- metin belgesine yazdıklarım ekranda çıksın istiyorum.
<code><span class="lit">cat metin.txt</span></code>
- metin.txt dosyasını /folder klasörüne kopyalamak/taşımak istiyorum.
<em>kopyalamak için:&nbsp;</em><code><span class="lit">cp -i ~/metin.txt ~/folder</span></code>
<em>(format: </em><code><span class="lit">cp -i [kopyalanacak dosya] [kopyalanacağı yer]</span></code><em>)</em>
<em>taşımak için:</em>&nbsp;<code><span class="lit">mv ~/metin.txt ~/folder</span></code>
<em>(format:&nbsp;</em><code><span class="lit">mv&nbsp;[kopyalanacak dosya] [kopyalanacağı yer]</span></code><em>)</em>
- folder klasörüne gitmek istiyorum.
<code><span class="lit">cd folder</span></code>
- metin.txt dosyasının ismini metin1.txt olarak değiştirmek istiyorum.
<code><span class="lit">mv metin.txt metin1.txt</span></code>
- metin1.txt dosyasını silmek istiyorum.
<code><span class="lit">rm metin1.txt</span></code>
-&nbsp;bir önceki klasöre (örneğin /a/b/c'den /a/b/'ye) gitmenin kısayolu?
<code><span class="lit">cd ..</span></code>
- açtığım folder klasörünü komple silmek istiyorum.
<em>kullanırken dikkatli olun, " silmek istediğinize emin misiniz" sorusunu sormaz!</em>
<code><span class="lit">rm -rf folder</span></code>
- internetten bir dosya indirmek istiyorum.
<em>bir metin belgesini wget komutunu kullanarak indireceğiz. wget, direkt olarak verdiğiniz linki indirir, bu yüzden direkt indirme bağlantıları vermelisiniz.
</em><code><span class="lit">wget https://www.le.ac.uk/oerresources/bdra/html/resources/example.txt</span></code>

yaptıklarımızı tekrar edelim: indirdiğiniz dosyayı <code><span class="lit">nano example.txt</span></code> ile açıp düzenleyebilirsiniz, ve <code><span class="lit">mv example.txt example2.txt</span></code> ile ismini example2.txt olarak değiştirebilirsiniz, <code><span class="lit">rm example2.txt</span></code> ile silebilirsiniz.
<h2><span style="color: #008000;">orta (2/3)</span></h2>
- her seferinde sudo yazmaktan bıktım. ubuntu'ya patronun kim olduğunu göstermek istiyorum, ne yapmalıyım?
<code><span class="lit">sudo -s</span></code>- geçmişte yazdığım komutları görmek istiyorum.
<code><span class="lit">cd ~</span></code><code><span class="lit">nano .bash_history</span></code>- hangi uygulamanın ne kadar ram, cpu kullandığını nasıl görebilirim? windows'taki görev yöneticine benzer bir şey var mı?
<em>var. htop kurun:&nbsp;</em><code><span class="lit">apt-get install htop</span></code>
<em>kullanın:</em> <code><span class="lit">htop</span></code>
<em>kapatın</em>: F10<em> (ya da ctrl+c)</em>
- iki komutu tek satırda nasıl yazarım?
komutların arasına <code><span class="lit">&amp;&amp;</span></code>&nbsp;koyarak. bir sonraki maddede örneği mevcut.
- bir dosyayı nasıl buluruz?&nbsp;CMakeLists.txt diye bir dosyayı arıyorum, aradım taradım yok, bütün klasörlere baktım bulamadım.
<code><span class="lit">updatedb &amp;&amp; locate -i CMakeLists.txt</span></code>
<h2><span style="color: #003366;">ileri (3/3)</span></h2>
- 80 portunu hangi uygulamalar kullanıyor? 80 portunu kullanmam lazım ama boşta görünmüyor, hatalar alıyorum.
<code><span class="lit">lsof -i :80</span></code>
- gireceğim komutun arkaplanda devamlı&nbsp;çalışmasını istiyorum, ne yapmalıyım?
<code><span class="lit">nohup [komut]&nbsp;&amp;</span></code>
örnek: <code><span class="lit">nohup ng serve --host 0.0.0.0 --port 80 --disable-host-check &amp;</span></code>
- arkaplandaki bu uygulamayı durdurmak, terminate etmek, çalışmasını sonlandırmak istiyorum.
<em>öncelikle arkaplanda çalışan bu uygulamanın PID değerini öğrenmemiz gerekiyor. </em><code><span class="lit">htop</span></code>&nbsp;<em>ile öğrenilebilir.</em>
<em>ardından:</em> <code><span class="lit">kill [PID]</span></code>&nbsp;<em>(örneğin:&nbsp;&nbsp;</em><code><span class="lit">kill 14508</span></code><em>)
</em>- tüm python işlemlerinin çalışmasını sonlandırmak istiyorum.
<code><span class="lit"><span class="pln">pkill </span><span class="pun">-</span><span class="lit">9&nbsp;</span><span class="pln">python</span></code>
