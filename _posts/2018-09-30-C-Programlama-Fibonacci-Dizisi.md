<!-- wp:paragraph -->
<p>Fibonacci dizisini yazdırmanın birçok yolu var. En son örnekte en basit hâlini yazdım.</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>#include &lt;stdio.h>

int main()
{
	int first = 1, second = 0, third;
	for (int n = 1; n &lt; 10; n++) {
		third = first + second;
		first = second;
		second = third;
		printf("%d\n", first);
	}
}</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>"n" yerine istediğiniz sayıyı girebilirsiniz. Bu sayıyı kullanıcıdan da isteyebiliriz:</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>#include &lt;stdio.h>

int main()
{
	int first = 1, second = 0, third, x;
	printf("Enter a number:");
	scanf("%d", &amp;x);
	for (int n = 1; n &lt;= x; n++) {
		third = first + second;
		first = second;
		second = third;
		printf("%d\n", first);
	}
}</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>Fonksiyon kullanılarak, farklı bir yöntemle şöyle de yapılabilir:</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>#include &lt;stdio.h>
int fibonacci(int);
int main()
{
	for (int i = 0; i &lt; 30; i++) {
		printf("%d ", fibonacci(i));
	}
	getch();
	return 0;
}
int fibonacci(int i) {
	if (i == 0)
		return 0;
	else if (i == 1)
		return 1;
	return fibonacci(i - 1) + fibonacci(i - 2);
}</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>Sadece iki integer tanımlayarak, 34'e kadar olan fibonacci sayılarını yazdırmanın yolu aşağıda. x'i 1 yaparak seriyi 1'den başlatabiliriz.</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>#include &lt;stdio.h>

int main(){
    int x = 0;
    int y = 1;
    while (x &lt;= 34){
        printf("%d %d ", x, y);
        x = x + y;
        y = x + y;
    }
}</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>Kodları deneyip compile etmek için online compiler: <a rel="noreferrer noopener" href="https://www.onlinegdb.com/online_c_compiler" target="_blank">https://www.onlinegdb.com/online_c_compiler</a></p>
<!-- /wp:paragraph -->