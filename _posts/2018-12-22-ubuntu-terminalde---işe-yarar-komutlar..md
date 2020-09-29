<h2><span style="color: #33cccc;">başlangıç (1/3)</span></h2>
dosya kopyalama, bir klasöre gitme, dosya silme gibi ufak tefek şeyler. sırasıyla yapabilirsiniz.

<strong>- bulunduğum klasörde neler var, nasıl görebilirim?
</strong><code><span class="lit">ls</span></code><strong>
- ana klasöre gitmek istiyorum.
</strong><code><span class="lit">cd ~/</span></code>
<em>(ya da yalnızca&nbsp;</em><code><span class="lit">cd</span></code><em>)</em><strong>
- bir klasör oluşturmak istiyorum. ismi folder olsun.
</strong><code>mkdir folder</code>
<strong>- bulunduğum klasöre metin.txt diye bir metin belgesi açıp bir şeyler yazmak istiyorum.
</strong><code>nano metin.txt</code>
<em>bir şeyler yazın.</em>
<em>kaydetmek için sırasıyla:</em> ctrl+x, y, enter
<strong>- metin belgesine yazdıklarım ekranda çıksın istiyorum.
</strong><code>cat metin.txt</code><strong>
</strong><strong>- metin.txt dosyasını /folder klasörüne kopyalamak/taşımak istiyorum.
</strong><em>kopyalamak için:&nbsp;</em><code><span class="lit">cp -i ~/metin.txt ~/folder</span></code>
<em>(format: </em><code><span class="lit">cp -i [kopyalanacak dosya] [kopyalanacağı yer]</span></code><em>)</em>
<em>taşımak için:</em>&nbsp;<code><span class="lit">mv ~/metin.txt ~/folder</span></code>
<em>(format:&nbsp;</em><code>mv&nbsp;[kopyalanacak dosya] [kopyalanacağı yer]</code><em>)</em>
<strong>- folder klasörüne gitmek istiyorum.
</strong><code>cd folder</code>
<strong>- metin.txt dosyasının ismini metin1.txt olarak değiştirmek istiyorum.</strong>
<code>mv metin.txt metin1.txt</code>
<strong>- metin1.txt dosyasını silmek istiyorum.
</strong><code>rm metin1.txt</code>
<strong>-&nbsp;bir önceki klasöre (örneğin /a/b/c'den /a/b/'ye) gitmenin kısayolu?
</strong><code>cd ..</code><strong>
- açtığım folder klasörünü komple silmek istiyorum.
</strong><em>kullanırken dikkatli olun, " silmek istediğinize emin misiniz" sorusunu sormaz!</em>
<code><span class="lit">rm -rf folder
</span></code><strong>- internetten bir dosya indirmek istiyorum.
</strong><em>bir metin belgesini wget komutunu kullanarak indireceğiz. wget, direkt olarak verdiğiniz linki indirir, bu yüzden direkt indirme bağlantıları vermelisiniz.
</em><code><span class="lit">wget https://www.le.ac.uk/oerresources/bdra/html/resources/example.txt</span></code>

yaptıklarımızı tekrar edelim: indirdiğiniz dosyayı <code><span class="lit">nano example.txt</span></code> ile açıp düzenleyebilirsiniz, ve <code><span class="lit">mv example.txt example2.txt</span></code> ile ismini example2.txt olarak değiştirebilirsiniz, <code><span class="lit">rm example2.txt</span></code> ile silebilirsiniz.
<h2><span style="color: #008000;">orta (2/3)</span></h2>
<strong>- her seferinde sudo yazmaktan bıktım. ubuntu'ya patronun kim olduğunu göstermek istiyorum, ne yapmalıyım?
</strong><code><span class="lit">sudo -s
</span></code><strong>- geçmişte yazdığım komutları görmek istiyorum.</strong>
<code><span class="lit">cd ~
</span></code><code><span class="lit">nano .bash_history
</span></code><strong>- hangi uygulamanın ne kadar ram, cpu kullandığını nasıl görebilirim? windows'taki görev yöneticine benzer bir şey var mı?
</strong><em>var. htop kurun:&nbsp;</em><code>apt-get install htop</code>
<em>kullanın:</em> <code>htop</code>
<em>kapatın</em>: F10<em> (ya da ctrl+c)</em>
<strong>- iki komutu tek satırda nasıl yazarım?</strong>
komutların arasına <code><span class="lit">&amp;&amp;</span></code>&nbsp;koyarak. bir sonraki maddede örneği mevcut.
<strong>- bir dosyayı nasıl buluruz?&nbsp;CMakeLists.txt diye bir dosyayı arıyorum, aradım taradım yok, bütün klasörlere baktım bulamadım.</strong>
<code><span class="lit">updatedb &amp;&amp; locate -i CMakeLists.txt</span></code>
<h2><span style="color: #003366;">ileri (3/3)</span></h2>
<strong>- 80 portunu hangi uygulamalar kullanıyor? 80 portunu kullanmam lazım ama boşta görünmüyor, hatalar alıyorum.</strong>
<code><span class="lit">lsof -i :80</span></code>
<strong>- gireceğim komutun arkaplanda devamlı&nbsp;çalışmasını istiyorum, ne yapmalıyım?
</strong><code><span class="lit">nohup [komut]&nbsp;&amp;</span></code>
örnek: <code><span class="lit">nohup ng serve --host 0.0.0.0 --port 80 --disable-host-check &amp;</span></code>
<strong>- arkaplandaki bu uygulamayı durdurmak, terminate etmek, çalışmasını sonlandırmak istiyorum.
</strong><em>öncelikle arkaplanda çalışan bu uygulamanın PID değerini öğrenmemiz gerekiyor. </em><code><span class="lit">htop</span></code>&nbsp;<em>ile öğrenilebilir.</em>
<em>ardından:</em> <code><span class="lit">kill [PID]</span></code>&nbsp;<em>(örneğin:&nbsp;&nbsp;</em><code><span class="lit">kill 14508</span></code><em>)
</em><strong>- tüm python işlemlerinin çalışmasını sonlandırmak istiyorum.</strong>
<code><span class="pln">pkill </span><span class="pun">-</span><span class="lit">9&nbsp;</span><span class="pln">python</span></code>