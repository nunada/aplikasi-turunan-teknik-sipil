@@ P43 | Latihan 43 | Kawat menjadi persegi dan segitiga | geometri | 344
Kawat 10 m dipotong dua menjadi persegi dan segitiga sama sisi. Kedua potongan harus terbentuk. Bagaimana memotong kawat agar total luas (a) maksimum, (b) minimum?
===
$x$ = bagian persegi:

$$A=\frac{x^2}{16}+\frac{\sqrt3}{36}(10-x)^2,\quad A'=\frac x8-\frac{\sqrt3}{18}(10-x)=0\Rightarrow x=\frac{40\sqrt3}{9+4\sqrt3}\approx4{,}35.$$

Ujung: $A(0)\approx4{,}81$, $A(10)=6{,}25$.

**Jawab:** (a) **maksimum tidak tercapai**, karena kedua potongan harus ada ($0<x<10$). Luas mendekati $6{,}25\ \text{m}^2$ ketika hampir seluruh kawat dipakai untuk persegi ($x\to10^-$). (b) Minimum tercapai bila $\approx4{,}35$ m dipakai untuk persegi.

Jika seluruh kawat diizinkan untuk satu bangun saja ($0\le x\le10$), maksimumnya $6{,}25\ \text{m}^2$ pada $x=10$.

@@ P44 | Latihan 44 | Kawat menjadi persegi dan lingkaran | geometri | 344
Ulangi latihan 43 (kedua potongan harus terbentuk) untuk persegi dan lingkaran.
===
$A=\dfrac{x^2}{16}+\dfrac{(10-x)^2}{4\pi}$, $A'=0\Rightarrow x=\dfrac{40}{4+\pi}\approx5{,}60$.

$A(0)\approx7{,}96$, $A(10)=6{,}25$.

**Jawab:** (a) **maksimum tidak tercapai** pada $0<x<10$. Luas mendekati $\dfrac{25}{\pi}\approx7{,}96\ \text{m}^2$ ketika hampir seluruh kawat dipakai untuk lingkaran ($x\to0^+$). (b) Minimum tercapai bila $\approx5{,}60$ m dipakai untuk persegi.

Jika seluruh kawat diizinkan untuk satu bangun saja, maksimumnya $\dfrac{25}{\pi}\ \text{m}^2$ pada $x=0$.

@@ P45 | Latihan 45 | Potongan pizza terbesar | geometri | 344
Satu juring pizza harus berkeliling 60 cm. Diameter pizza berapa yang memberi juring terluas?
===
$2r+r\theta=60$, $A=\tfrac12r^2\theta=30r-r^2$, $A'=0\Rightarrow r=15$.

**Jawab:** diameter $30$ cm ($\theta=2$ rad).

@@ P46 | Latihan 46 | Tangga terpendek melewati pagar | struktur | 344
Pagar setinggi 2 m sejajar gedung pada jarak 1 m. Berapa panjang tangga terpendek dari tanah, melewati pagar, ke dinding gedung?

{{fig:s_p46}}
===
$$L(\theta)=\frac{2}{\sin\theta}+\frac{1}{\cos\theta},\quad L'=0\Rightarrow\tan^3\theta=2.$$

**Jawab:** $L_{\min}=\left(1+2^{2/3}\right)^{3/2}\approx4{,}16$ m.

@@ P47 | Latihan 47 | Gelas kerucut dari lingkaran kertas | volume | 344
Gelas kerucut dibuat dari kertas lingkaran berjari-jari $R$ dengan memotong juring lalu menyambung $CA$ dan $CB$. Tentukan kapasitas maksimum.

{{fig:s_p47}}
===
$h=\sqrt{R^2-r^2}$, $V=\dfrac\pi3r^2h$. Dalam $h$: $V=\dfrac\pi3(R^2-h^2)h$, $V'=0\Rightarrow h=R/\sqrt3$.

**Jawab:** $V_{\max}=\dfrac{2\pi R^3}{9\sqrt3}$.

@@ P48 | Latihan 48 | Gelas kerucut dengan kertas minimum | volume | 345
Gelas kertas kerucut harus memuat $27\ \text{cm}^3$. Tentukan tinggi dan jari-jari dengan kertas paling sedikit.
===
$h=\dfrac{81}{\pi r^2}$, $S^2=\pi^2r^2(r^2+h^2)=\pi^2r^4+\dfrac{81^2}{r^2}$.

Turunan nol: $r^6=\dfrac{81^2}{2\pi^2}$.

**Jawab:** $r\approx2{,}63$ cm, $h=\sqrt2\thinspace r\approx3{,}72$ cm.

@@ P49 | Latihan 49 | Kerucut terbalik di dalam kerucut | volume | 345
Kerucut setinggi $h$ berada dalam kerucut setinggi $H$ dengan puncaknya di pusat alas kerucut besar. Tunjukkan volume terbesar saat $h=H/3$.

{{fig:s_p49}}
===
Alas kerucut dalam setinggi $h$, jari-jarinya $R(1-h/H)$:

$$V=\frac\pi3R^2\left(1-\frac hH\right)^2h,\quad V'=\frac\pi3R^2\left(1-\frac hH\right)\left(1-\frac{3h}{H}\right)=0.$$

$V=0$ di $h=0$ dan $h=H$, jadi maksimum di $h=H/3$. $\blacksquare$

@@ P50 | Latihan 50 | Gaya tarik minimum melawan gesekan | gerak | 345
Gaya untuk menyeret benda berberat $W$ dengan tali bersudut $\theta$: $F=\dfrac{\mu W}{\mu\sin\theta+\cos\theta}$. Sudut berapa membuat $F$ terkecil?

{{fig:s_p50}}
===
Maksimumkan penyebut $g=\mu\sin\theta+\cos\theta$: $g'=\mu\cos\theta-\sin\theta=0\Rightarrow\tan\theta=\mu$.

**Jawab:** $\theta=\arctan\mu$, $F_{\min}=\dfrac{\mu W}{\sqrt{1+\mu^2}}$.

@@ P54 | Latihan 54 | Dua perahu paling dekat | lintasan | 345
Pukul 14.00 sebuah perahu meninggalkan dermaga ke selatan 20 km/jam. Perahu lain yang bergerak ke timur 15 km/jam tiba di dermaga itu pukul 15.00. Kapan keduanya paling dekat?
===
$t$ jam setelah 14.00: $D^2=225(1-t)^2+400t^2$. Turunan $-450(1-t)+800t=0\Rightarrow t=0{,}36$ jam.

**Jawab:** pukul 14.21.36.

@@ P55 | Latihan 55 | Variasi soal menyeberang sungai | lintasan | 345
Selesaikan Contoh 4 untuk sungai selebar 5 km dan $B$ hanya 5 km ke hilir.
===
$T=\dfrac{\sqrt{x^2+25}}{6}+\dfrac{5-x}{8}$, $0\le x\le5$. Titik kritis $x=15/\sqrt7\approx5{,}67$ berada di luar domain dan $T'<0$.

**Jawab:** dayung **langsung ke $B$** ($T=\sqrt{50}/6\approx1{,}18$ jam).

@@ P56 | Latihan 56 | Mengitari danau lingkaran | lintasan | 345
Seseorang di tepi danau berjari-jari 3 km ingin ke titik seberang diametral secepatnya. Ia berjalan 6 km/jam dan mendayung 3 km/jam. Bagaimana caranya?

{{fig:s_p56}}
===
Mendayung tali busur $6\cos\theta$, lalu berjalan busur $6\theta$:

$$T=2\cos\theta+\theta,\quad0\le\theta\le\frac\pi2.$$

$T'=1-2\sin\theta=0$ di $\theta=\pi/6$ yang ternyata **maksimum**. Ujung: $T(0)=2$, $T(\pi/2)=\pi/2\approx1{,}57$.

**Jawab:** berjalan kaki seluruhnya mengelilingi danau.

@@ P57 | Latihan 57 | Rute pipa kilang minyak | biaya | 345
Kilang di tepi utara sungai selebar 2 km; tangki di tepi selatan 6 km ke timur. Pipa darat 400 ribu dolar/km, pipa bawah sungai 800 ribu dolar/km. Di mana titik $P$ (tepi utara) agar biaya minimum?

{{fig:s_p57}}
===
$P$ berjarak $x$ km dari kilang (ribu dolar):

$$C=400x+800\sqrt{(6-x)^2+4}.$$

$$C'=0\iff\sqrt{(6-x)^2+4}=2(6-x)\Rightarrow6-x=\frac{2}{\sqrt3}.$$

**Jawab:** $x=6-\dfrac{2}{\sqrt3}\approx4{,}85$ km dari kilang.

@@ P58 | Latihan 58 | Kilang 1 km dari sungai | biaya | 345
Pada latihan 57, kilang berada 1 km di utara sungai. Di mana $P$?

{{fig:s_p58}}
===
$$C=400\sqrt{x^2+1}+800\sqrt{(6-x)^2+4}.$$

$$\frac{x}{\sqrt{x^2+1}}=\frac{2(6-x)}{\sqrt{(6-x)^2+4}}.$$

Diselesaikan numerik: $x\approx4{,}88$.

**Jawab:** sekitar $4{,}88$ km di timur titik tepi sungai terdekat ke kilang.

@@ P59 | Latihan 59 | Penerangan minimum antara dua sumber | struktur | 345–346
Penerangan sebanding dengan kuat sumber dan berbanding terbalik dengan kuadrat jarak. Dua sumber berjarak 4 m, satu tiga kali lebih kuat. Di mana penerangan paling kecil?

{{fig:s_p59}}
===
$I=\dfrac{3k}{x^2}+\dfrac{k}{(4-x)^2}$, $I'=0\Rightarrow x=\sqrt[3]3\thinspace (4-x)$.

**Jawab:** $x=\dfrac{4\sqrt[3]3}{1+\sqrt[3]3}\approx2{,}36$ m dari sumber kuat.

@@ P60 | Latihan 60 | Garis yang memotong luas terkecil | geometri | 346
Tentukan persamaan garis melalui $(3; 5)$ yang memotong luas terkecil dari kuadran pertama.
===
Intersep $a,b$: $\dfrac3a+\dfrac5b=1\Rightarrow b=\dfrac{5a}{a-3}$. $A=\dfrac{5a^2}{2(a-3)}$, $A'=0\Rightarrow a=6$, $b=10$.

**Jawab:** $y=-\tfrac53x+10$ (luas $30$).

@@ P61 | Latihan 61 | Ruas garis terpendek melalui (a, b) | geometri | 346
Tentukan panjang ruas terpendek yang dipotong kuadran pertama dan melalui $(a,b)$, $a,b>0$.
===
$L(\theta)=\dfrac{a}{\cos\theta}+\dfrac{b}{\sin\theta}$, $L'=0\Rightarrow\tan^3\theta=b/a$.

**Jawab:** $\left(a^{2/3}+b^{2/3}\right)^{3/2}$.

@@ P62 | Latihan 62 | Garis singgung paling curam | dasar | 346
Di titik mana pada $y=1+40x^3-3x^5$ garis singgung memiliki gradien terbesar?
===
$m=120x^2-15x^4$, $m'=60x(4-x^2)=0$. $m(\pm2)=240$ (maksimum).

**Jawab:** $(2; 225)$ dan $(-2; -223)$.

@@ P63 | Latihan 63 | Ruas singgung terpendek hiperbola | geometri | 346
Berapa panjang terpendek ruas garis singgung $y=3/x$ yang dipotong kuadran pertama?
===
Singgung di $(a,3/a)$: intersep $2a$ dan $6/a$. $L^2=4a^2+\dfrac{36}{a^2}$, minimum saat $a^2=3$.

**Jawab:** $L=2\sqrt6$.

@@ P64 | Latihan 64 | Segitiga singgung terkecil parabola | geometri | 346
Berapa luas terkecil segitiga di kuadran pertama yang sisi miringnya menyinggung $y=4-x^2$?
===
Singgung di $x=a$: $y=-2ax+a^2+4$. $A=\dfrac{(a^2+4)^2}{4a}$, $A'=0\Rightarrow3a^2=4$.

**Jawab:** $A_{\min}=\dfrac{32\sqrt3}{9}\approx6{,}16$.

@@ P71 | Latihan 71 | Segitiga sama kaki dengan keliling tetap | dasar | 346
Tunjukkan di antara segitiga sama kaki berkeliling $p$, yang terluas adalah sama sisi.
===
Kaki $a$, alas $p-2a$:

$$A^2=\frac{p}{16}(p-2a)^2(4a-p),\qquad\frac p4<a<\frac p2.$$

$\dfrac{d}{da}\big[(p-2a)^2(4a-p)\big]=4(p-2a)(2p-6a)=0\Rightarrow a=\dfrac p3$.

Ketiga sisi sama. $\blacksquare$

@@ P72 | Latihan 72 | Pipa tidak pernah tegak lurus sungai | biaya | 346
Pada latihan 57, andaikan biaya bawah sungai $k$ jauh lebih mahal daripada darat. Tunjukkan $P$ **tidak pernah** optimal tepat di seberang tangki.
===
$C(x)=400x+k\sqrt{(6-x)^2+4}$, sehingga

$$C'(x)=400-\frac{k(6-x)}{\sqrt{(6-x)^2+4}},\qquad C'(6)=400>0.$$

$C$ masih naik di $x=6$, jadi sedikit ke barat selalu lebih murah, berapa pun $k$. $\blacksquare$

@@ P73 | Latihan 73 | Garis singgung elips | geometri | 346
Garis singgung elips $x^2/a^2+y^2/b^2=1$ di $(p,q)$ kuadran pertama. (a) Tunjukkan intersepnya $a^2/p$ dan $b^2/q$. (b) Panjang minimumnya $a+b$. (c) Luas segitiga minimumnya $ab$.
===
(a) Garis singgung: $\dfrac{px}{a^2}+\dfrac{qy}{b^2}=1$; nolkan $y$ atau $x$.

(b) $p=a\cos t$, $q=b\sin t$:

$$L^2=\frac{a^2}{\cos^2t}+\frac{b^2}{\sin^2t}.$$

Turunan nol saat $\tan^4t=b^2/a^2$, memberi $L^2=(a+b)^2$.

(c) $A=\dfrac{a^2b^2}{2pq}=\dfrac{ab}{\sin2t}\ge ab$, tercapai di $t=\pi/4$. $\blacksquare$

@@ P74 | Latihan 74 | Rangka layang-layang | struktur | 346
Rangka layang-layang: empat batang luar $a,a,b,b$. Panjang diagonal berapa yang memaksimumkan luas?

{{fig:s_p74}}
===
Luas = dua kali segitiga bersisi $a,b$ dengan sudut apit $\gamma$: $A=ab\sin\gamma$, maksimum di $\gamma=90^\circ$.

**Jawab:** diagonal sumbu $\sqrt{a^2+b^2}$, diagonal lainnya $\dfrac{2ab}{\sqrt{a^2+b^2}}$.

@@ P75 | Latihan 75 | Titik sambung kabel dengan panjang minimum | struktur | 346
Titik $P$ pada $AD$ dihubungkan dengan kabel ke $A$, $B$, dan $C$. Nyatakan panjang total $L$ dalam $x=|AP|$ dan perkirakan nilai minimumnya.

{{fig:s_p75}}
===
$$L(x)=x+\sqrt{(5-x)^2+4}+\sqrt{(5-x)^2+9},\qquad0\le x\le5.$$

Grafik $L'$ memotong nol di $x\approx3{,}59$.

**Jawab:** $L_{\min}\approx9{,}35$ m.

@@ P76 | Latihan 76 | Laju hemat bahan bakar | gerak | 347
Grafik konsumsi bahan bakar $c(v)$ (liter/jam) terhadap laju diberikan. Perkirakan laju yang meminimumkan konsumsi per kilometer $G$.

{{fig:s_p76}}
===
$G(v)=\dfrac{c(v)}{v}$, sehingga $G'=0\iff c'(v)=\dfrac{c(v)}{v}$: garis dari titik asal **menyinggung** kurva.

**Jawab:** dari grafik, sekitar $v\approx85$ km/jam (perkiraan baca grafik), lebih tinggi daripada laju yang meminimumkan $c$.

@@ P77 | Latihan 77 | Hukum Snell udara–air | lintasan | 347
Cahaya dari $A$ (udara, laju $v_1$) ke $B$ (air, laju $v_2$) melalui $C$ dengan waktu minimum. Tunjukkan $\dfrac{\sin\theta_1}{\sin\theta_2}=\dfrac{v_1}{v_2}$.

{{fig:s_p77}}
===
Jarak tegak $a,b$ dan jarak datar total $d$:

$$T(x)=\frac{\sqrt{a^2+x^2}}{v_1}+\frac{\sqrt{b^2+(d-x)^2}}{v_2}.$$

$$T'=\frac{\sin\theta_1}{v_1}-\frac{\sin\theta_2}{v_2}=0.$$

$T''>0$, jadi minimum, dan rasio yang diminta mengikuti. $\blacksquare$

@@ P78 | Latihan 78 | Tali terpendek antara dua tiang | struktur | 347
Tali dari puncak tiang $PQ$ ke titik tanah $R$ lalu ke puncak tiang $ST$. Tunjukkan panjangnya minimum saat $\theta_1=\theta_2$.

{{fig:s_p78}}
===
Tinggi tiang $p,s$, jarak $d$, $QR=x$:

$$L=\sqrt{x^2+p^2}+\sqrt{(d-x)^2+s^2}.$$

$$L'=\frac{x}{\sqrt{x^2+p^2}}-\frac{d-x}{\sqrt{(d-x)^2+s^2}}=\cos\theta_1-\cos\theta_2=0.$$

Karena sudutnya lancip, $\theta_1=\theta_2$. $\blacksquare$

@@ P79 | Latihan 79 | Lipatan kertas terpendek | geometri | 347
Sudut kanan atas kertas $30\times20$ cm dilipat hingga menyentuh tepi bawah. Pilih $x$ agar panjang lipatan $y$ minimum.

{{fig:s_p79}}
===
Bayangan sudut berjarak $d$ dari sudut kanan bawah: $d^2=x^2-(20-x)^2=40(x-10)$. Potongan lipatan di tepi atas $a=20x/d$. Maka

$$y^2=x^2+a^2=\frac{x^3}{x-10},\qquad10<x\le20.$$

Turunan nol: $x^2(2x-30)=0\Rightarrow x=15$.

**Jawab:** $x=15$ cm, $y=15\sqrt3\approx25{,}98$ cm ($a\approx21{,}2\le30$, muat).

@@ P80 | Latihan 80 | Pipa terpanjang melewati belokan lorong | struktur | 347
Pipa baja dibawa horizontal dari lorong selebar 3 m berbelok siku ke lorong 2 m. Berapa panjang pipa terpanjang yang bisa lewat?

{{fig:s_p80}}
===
Panjang ruas yang menyentuh sudut dalam:

$$L(\theta)=\frac{3}{\sin\theta}+\frac{2}{\cos\theta}.$$

Pipa terpanjang = **minimum** $L$: $\tan^3\theta=\tfrac32$.

**Jawab:** $\left(3^{2/3}+2^{2/3}\right)^{3/2}\approx7{,}02$ m.

@@ P81 | Latihan 81 | Sudut pandang maksimum dua pelari | gerak | 347
Pengamat berjarak 1 satuan dari lintasan. Dua pelari mulai dari $S$; satu tiga kali lebih cepat. Tentukan sudut pandang $\theta$ maksimum.

{{fig:s_p81}}
===
$\theta=\arctan3t-\arctan t$, $\theta'=\dfrac{3}{1+9t^2}-\dfrac{1}{1+t^2}=0\Rightarrow t=\dfrac1{\sqrt3}$.

**Jawab:** $\theta_{\max}=\dfrac\pi6=30^\circ$.

@@ P82 | Latihan 82 | Talang air dari lembaran logam | air | 347
Lembaran selebar 30 cm dibengkokkan sepertiga di tiap sisi dengan sudut $\theta$. $\theta$ berapa agar talang mengalirkan air terbanyak?

{{fig:s_p82}}
===
$A=\tfrac12(10+10+20\cos\theta)(10\sin\theta)=100\sin\theta(1+\cos\theta)$.

$$A'=100(\cos\theta+\cos2\theta)=0\Rightarrow\theta=\frac\pi3.$$

**Jawab:** $\theta=60^\circ$ ($A\approx129{,}9\ \text{cm}^2$).

@@ P83 | Latihan 83 | Memaksimumkan sudut pada ruas garis | geometri | 348
Di mana $P$ pada $AB$ dipilih agar sudut $\theta$ maksimum?

{{fig:s_p83}}
===
$x=BP$: $\theta=\pi-\arctan\dfrac2x-\arctan\dfrac{5}{3-x}$.

$$\theta'=\frac{2}{x^2+4}-\frac{5}{(3-x)^2+25}=0\iff x^2+4x-16=0.$$

**Jawab:** $BP=2\sqrt5-2\approx2{,}47$.

@@ P84 | Latihan 84 | Jarak pandang terbaik ke lukisan | geometri | 348
Lukisan setinggi $h$ dengan tepi bawah $d$ di atas mata. Pengamat sebaiknya berdiri sejauh berapa?

{{fig:s_p84}}
===
$\theta=\arctan\dfrac{h+d}{x}-\arctan\dfrac dx$,

$$\theta'=-\frac{h+d}{x^2+(h+d)^2}+\frac{d}{x^2+d^2}=0.$$

**Jawab:** $x=\sqrt{d(h+d)}$.

@@ P85 | Latihan 85 | Persegi panjang luar terbesar | geometri | 348
Tentukan luas maksimum persegi panjang luar yang setiap sisinya melalui satu titik sudut persegi panjang dalam berukuran $L\times W$ (petunjuk: gunakan sudut $\theta$).

{{fig:s_p85}}
===
$$A(\theta)=(L\cos\theta+W\sin\theta)(L\sin\theta+W\cos\theta)=LW+\frac{L^2+W^2}{2}\sin2\theta.$$

Maksimum di $\theta=45^\circ$.

**Jawab:** $\dfrac{(L+W)^2}{2}$.

@@ P88 | Latihan 88 | Penerangan dari dua lampu identik | struktur | 349
Dua lampu identik berjarak 10 m. Titik $P$ berada pada garis sejajar sejauh $d$ meter, dengan posisi $0\le x\le10$. (a) Tulis $I(x)$. (b) Untuk $d=5$ m, minimum di tengah. (c) Untuk $d=10$ m, minimum bukan di tengah. (d) Tentukan nilai peralihan $d$.

{{fig:s_p88}}
===
(a) $I(x)=k\left[\dfrac{1}{x^2+d^2}+\dfrac{1}{(10-x)^2+d^2}\right]$.

(b) $d=5$: titik kritis pada $0\le x\le10$ adalah $x=5$ serta $x\approx0{,}45$ dan $x\approx9{,}55$. Dua titik terakhir merupakan **maksimum lokal** ($I\approx0{,}0483k$). Untuk minimum mutlak, bandingkan titik tengah dengan kedua ujung: $I(5)=0{,}040k<I(0)=I(10)=0{,}048k$, sehingga minimum mutlak di $x=5$.

### Letak minimum untuk setiap $d>0$

Misalkan $u=(x-5)^2$ dengan $0\le u\le25$, dan $c=25+d^2$. Maka

$$\frac{I}{k}=\frac{2(u+c)}{(u+c)^2-100u},$$

$$\frac{d}{du}\left(\frac Ik\right)=\frac{2\left[100c-(u+c)^2\right]}{\left[(u+c)^2-100u\right]^2}.$$

Pembilang $100c-(u+c)^2$ selalu turun terhadap $u$, sehingga tandanya berubah paling banyak sekali, dari positif ke negatif. Jadi setiap titik kritis interior terhadap $u$ merupakan **maksimum**. Akibatnya minimum mutlak selalu terjadi di $u=0$ (titik tengah, $x=5$) atau di $u=25$ (ujung, $x=0$ atau $x=10$).

(c) $d=10$: cukup bandingkan $I(0)=I(10)=0{,}015k$ dengan $I(5)=0{,}016k$. Minimum mutlak ada di ujung, bukan di tengah.

(d) Bandingkan nilai di ujung dan di tengah:

$$I(0)-I(5)=\frac{50k\thinspace (50-d^2)}{d^2(d^2+25)(d^2+100)}.$$

Untuk $d^2<50$ minimum ada di tengah, sedangkan untuk $d^2>50$ minimum ada di ujung.

**Jawab:** peralihan terjadi pada $d=5\sqrt2\approx7{,}07$ m.

@@ L1 | Proyek Kaleng 1 | Tutup dipotong dari persegi | volume | 349
Volume $V$ tetap; selimut tanpa sisa, tetapi tutup dan alas dipotong dari persegi sisi $2r$. Tunjukkan bahan minimum saat $h/r=8/\pi$.

{{fig:s_can1}}
===
$A=8r^2+2\pi rh=8r^2+\dfrac{2V}{r}$, $A'=16r-\dfrac{2V}{r^2}=0\Rightarrow V=8r^3$.

$\dfrac hr=\dfrac{V}{\pi r^3}=\dfrac8\pi\approx2{,}55$. $\blacksquare$

@@ L2 | Proyek Kaleng 2 | Tutup dipotong dari heksagon | volume | 349
Jika tutup dan alas dipotong dari heksagon, tunjukkan $h/r=4\sqrt3/\pi$.

{{fig:s_can2}}
===
Heksagon dengan lingkaran dalam berjari-jari $r$ luasnya $2\sqrt3r^2$, dua buah $4\sqrt3r^2$:

$$A=4\sqrt3r^2+\frac{2V}{r},\quad A'=0\Rightarrow V=4\sqrt3r^3.$$

$\dfrac hr=\dfrac{4\sqrt3}{\pi}\approx2{,}21$. $\blacksquare$

@@ L3 | Proyek Kaleng 3 | Memasukkan biaya sambungan | biaya | 349–350
Biaya total sebanding dengan $4\sqrt3r^2+2\pi rh+k(4\pi r+h)$. Tunjukkan minimum tercapai saat $\dfrac{\sqrt[3]V}{k}=\sqrt[3]{\dfrac{\pi h}{r}}\cdot\dfrac{2\pi-h/r}{\pi h/r-4\sqrt3}$.
===
Dengan $h=V/(\pi r^2)$:

$$f(r)=4\sqrt3r^2+\frac{2V}{r}+k\left(4\pi r+\frac{V}{\pi r^2}\right).$$

$$f'=8\sqrt3r-\frac{2V}{r^2}+4\pi k-\frac{2kV}{\pi r^3}=0.$$

Substitusi $V=\pi r^2h$ dan $q=h/r$ menyederhanakannya menjadi $k(2\pi-q)=r(\pi q-4\sqrt3)$. Karena $\sqrt[3]V=r\sqrt[3]{\pi q}$:

$$\frac{\sqrt[3]V}{k}=\sqrt[3]{\pi q}\cdot\frac{2\pi-q}{\pi q-4\sqrt3}.\qquad\blacksquare$$

@@ L4 | Proyek Kaleng 4 | Membaca grafik rasio optimum | biaya | 350
Gambarkan grafik $\sqrt[3]V/k$ sebagai fungsi $x=h/r$ dan jelaskan pengaruh ukuran kaleng serta biaya sambungan.

{{fig:s_can4}}
===
Fungsi $g(x)=\sqrt[3]{\pi x}\thinspace \dfrac{2\pi-x}{\pi x-4\sqrt3}$ turun dari tak hingga (saat $x\to4\sqrt3/\pi\approx2{,}21$) menuju $0$ (saat $x=2\pi$).

- Kaleng besar atau sambungan murah ($\sqrt[3]V/k$ besar): $h/r$ mendekati $2{,}21$.
- Kaleng kecil atau sambungan mahal ($\sqrt[3]V/k$ kecil): $h/r$ jauh lebih besar, kaleng lebih langsing.

@@ L5 | Proyek Kaleng 5 | Diskusi bentuk kaleng nyata | biaya | 350
Apakah kaleng besar yang hampir "persegi" dan kaleng kecil yang tinggi langsing sesuai kenyataan? Mengapa ada pengecualian?
===
Pertanyaan terbuka. Secara umum kaleng kecil memang cenderung relatif lebih tinggi. Pengecualian dapat muncul karena faktor yang tidak ada dalam model: kemudahan membuka dan mengambil isi (misalnya kaleng ikan yang pendek), stabilitas tumpukan, ukuran rak dan kemasan, tampilan label, ketebalan pelat yang berbeda untuk tutup, serta standar mesin produksi.

Pelajaran untuk perancangan teknik: hasil optimum hanya sebaik fungsi tujuan dan kendala yang dimasukkan ke model.
