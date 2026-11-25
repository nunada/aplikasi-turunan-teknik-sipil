@@ P41 | Latihan 41 | Jarak vertikal dan horizontal dua grafik | lintasan | 285
Untuk grafik $y=2x+3$ dan $y=\ln x$, tentukan (a) jarak vertikal minimum, (b) jarak horizontal minimum.

{{fig:h_p41}}
===
(a) $D=2x+3-\ln x$, $D'=2-\dfrac1x=0\Rightarrow x=\tfrac12$. $D_{\min}=4+\ln2\approx4{,}69$.

(b) Pada ketinggian $y$: $H(y)=e^y-\dfrac{y-3}{2}$, $H'=e^y-\tfrac12=0\Rightarrow y=-\ln2$. $H_{\min}=\dfrac{4+\ln2}{2}\approx2{,}35$.

@@ P42 | Latihan 42 | Titik dengan kemiringan terbesar | dasar | 285
Tentukan titik pada $y=20x^3+60x-3x^5-5x^4$ yang kemiringannya terbesar.
===
Kemiringan $m=60+60x^2-20x^3-15x^4$ dan $m'=-60x(x+2)(x-1)$.

$m(-2)=220$, $m(0)=60$, $m(1)=85$, dan $m\to-\infty$ untuk $x\to\pm\infty$.

**Jawab:** titik $(-2;\,-264)$ dengan kemiringan $220$.

@@ P43 | Latihan 43 | Segitiga terkecil oleh garis singgung parabola | geometri | 285
Di antara segitiga di kuadran pertama yang dibentuk sumbu koordinat dan garis singgung $y=3x-x^2$, berapa luas terkecil?

{{fig:h_p43}}
===
Garis singgung di $x=a$: $y=(3-2a)x+a^2$. Untuk $a>\tfrac32$: titik potong $x=\dfrac{a^2}{2a-3}$, $y=a^2$.

$$A(a)=\frac{a^4}{2(2a-3)},\quad A'\propto a^3(6a-12)=0\Rightarrow a=2.$$

**Jawab:** luas minimum $8$.

@@ P44 | Latihan 44 | Kerucut dari lingkaran yang dipotong juring | volume | 286
Kerucut dibuat dari lingkaran berjari-jari 1 m dengan membuang juring bersudut $\theta$ lalu menyambung kedua tepinya. Tentukan volume terbesar.

{{fig:h_p44}}
===
Garis pelukis $1$, jadi $h=\sqrt{1-r^2}$ dengan $r=1-\dfrac{\theta}{2\pi}$. $V=\dfrac\pi3r^2\sqrt{1-r^2}$. Dengan $u=r^2$, maksimumkan $u^2(1-u)$: $u=\tfrac23$.

**Jawab:** $V_{\max}=\dfrac{2\pi}{9\sqrt3}\approx0{,}403\ \text{m}^3$, saat $\theta=2\pi\left(1-\sqrt{2/3}\right)\approx66^\circ$.

@@ P45 | Latihan 45 | Gerak vertikal | gerak | 286
Tinggi benda $s=-4{,}9t^2+29{,}4t+34{,}3$ (m, s). Tentukan (a) kecepatan saat $t=0$; (b) tinggi maksimum dan waktunya; (c) kecepatan saat $s=0$.
===
$v=-9{,}8t+29{,}4$.

(a) $v(0)=29{,}4$ m/s.

(b) $v=0\Rightarrow t=3$ s, $s=78{,}4$ m.

(c) $s=0\iff t^2-6t-7=0\Rightarrow t=7$; $v(7)=-39{,}2$ m/s.

@@ P46 | Latihan 46 | Rute tercepat dari perahu ke desa | lintasan | 286
Jane berada 2 km lepas pantai dan ingin ke desa yang berjarak 6 km sepanjang pantai lurus dari titik terdekat. Ia mendayung 2 km/jam dan berjalan 5 km/jam. Di mana ia harus mendarat?

{{fig:h_p46}}
===
$$T(x)=\frac{\sqrt{4+x^2}}{2}+\frac{6-x}{5},\quad T'=\frac{x}{2\sqrt{4+x^2}}-\frac15=0\Rightarrow21x^2=16.$$

**Jawab:** mendarat $x=\dfrac{4}{\sqrt{21}}\approx0{,}87$ km dari titik terdekat ke arah desa.

@@ P47 | Latihan 47 | Balok penopang terpendek melewati tembok | struktur | 286
Tembok setinggi 2 m berjarak 5 m dari gedung. Berapa panjang balok lurus terpendek dari tanah di luar tembok yang mencapai dinding gedung?

{{fig:h_p47}}
===
Sudut balok terhadap tanah $\theta$:

$$L(\theta)=\frac{2}{\sin\theta}+\frac{5}{\cos\theta},\quad L'=0\Rightarrow\tan^3\theta=\frac25.$$

**Jawab:** $L_{\min}=\left(2^{2/3}+5^{2/3}\right)^{3/2}\approx9{,}58$ m ($\theta\approx36{,}4^\circ$).

@@ P48 | Latihan 48 | Dua partikel pada satu garis | gerak | 286
Posisi dua partikel: $s_1=\sin t$, $s_2=\sin(t+\pi/3)$. (a) Kapan bertemu pada $0\le t\le2\pi$? (b) Jarak terjauh? (c) Kapan besar kecepatan relatif kedua partikel maksimum pada $0\le t\le2\pi$?
===
$s_1-s_2=-\cos(t+\pi/6)$.

(a) $\cos(t+\pi/6)=0\Rightarrow t=\dfrac\pi3,\ \dfrac{4\pi}{3}$.

(b) Jarak maksimum $1$ m.

(c) Kecepatan relatif $v_1-v_2=\dfrac{d}{dt}(s_1-s_2)=\sin(t+\pi/6)$. Besarnya $|\sin(t+\pi/6)|$ maksimum, yaitu $1$ m/s, di $t=\dfrac\pi3;\,\dfrac{4\pi}{3}$, saat keduanya berpapasan.

**Catatan:** jarak $D(t)=|\cos(t+\pi/6)|$ **tidak dapat diturunkan** di kedua waktu itu (grafiknya bersudut). Untuk $D\ne0$ berlaku $|D'(t)|=|\sin(t+\pi/6)|$, yang **mendekati** $1$ saat $t$ mendekati waktu pertemuan.

@@ P49 | Latihan 49 | Penerangan minimum di antara dua lampu | struktur | 286
Intensitas penerangan sebanding dengan kebalikan kuadrat jarak. Dua lampu berjarak 6 m, satu delapan kali lebih kuat. Seberapa jauh dari lampu kuat penerangan total minimum?

{{fig:h_p49}}
===
$$I(x)=\frac{8k}{x^2}+\frac{k}{(6-x)^2},\quad I'=-\frac{16k}{x^3}+\frac{2k}{(6-x)^3}=0\Rightarrow x=2(6-x).$$

**Jawab:** $4$ m dari lampu yang kuat.

@@ P50 | Latihan 50 | Jangkauan peluru maksimum | gerak | 286
Jangkauan peluru $R=\dfrac{v_0^2}{g}\sin2\alpha$. Tentukan sudut $\alpha$ yang memaksimumkannya.

{{fig:h_p50}}
===
$R'(\alpha)=\dfrac{2v_0^2}{g}\cos2\alpha=0\Rightarrow\alpha=\dfrac\pi4$ pada $[0;\,\pi/2]$.

**Jawab:** $45^\circ$.

@@ P51 | Latihan 51 | Balok kayu terkuat dari gelondongan | struktur | 286
Kekuatan balok persegi panjang $S=kwd^2$. (a) Dimensi balok terkuat dari gelondongan berdiameter 30 cm? (b)–(c) Gambarkan grafik $S$ terhadap $w$ dan $d$ ($k=1$); apa pengaruh $k$?

{{fig:h_p51}}
===
(a) $d^2=900-w^2$, $S=kw(900-w^2)$, $S'=k(900-3w^2)=0$.

**Jawab:** $w=10\sqrt3\approx17{,}3$ cm, $d=10\sqrt6\approx24{,}5$ cm, yaitu $d/w=\sqrt2$.

(b)–(c)

{{fig:h_p51g h_p51h}}

Kedua grafik mencapai puncak sama tinggi, di $w\approx17{,}3$ dan $d\approx24{,}5$. Mengubah $k$ hanya menskalakan tinggi grafik; letak maksimum tidak berubah.

@@ P52 | Latihan 52 | Balok paling kaku dari gelondongan | struktur | 286
Kekakuan balok $S=kwd^3$. (a) Dimensi balok terkaku dari gelondongan berdiameter 30 cm? (b)–(c) Grafik terhadap $w$ dan $d$.

{{fig:h_p51}}
===
(a) Maksimumkan $S=kd^3\sqrt{900-d^2}$:

$$S'=\frac{kd^2\,(3(900-d^2)-d^2)}{\sqrt{900-d^2}}=0\Rightarrow d^2=675.$$

**Jawab:** $w=15$ cm, $d=15\sqrt3\approx26{,}0$ cm.

(b)–(c)

{{fig:h_p52g h_p52h}}

Puncak di $w=15$ dan $d\approx26$; nilai $k$ hanya mengubah skala.

@@ P53 | Latihan 53 | Kereta pada pegas | gerak | 286
Posisi kereta $s=10\cos\pi t$ (cm), $0\le t\le4$. (a) Laju maksimum, kapan, di mana, dan percepatannya? (b) Di mana kereta saat besar percepatan maksimum, dan berapa lajunya saat itu?

{{fig:h_p53}}
===
$v=-10\pi\sin\pi t$, $a=-10\pi^2\cos\pi t$.

(a) $|v|_{\max}=10\pi\approx31{,}4$ cm/s pada $t=0{,}5;\,1{,}5;\,2{,}5;\,3{,}5$ s, di $s=0$, saat itu $a=0$.

(b) $|a|_{\max}=10\pi^2\approx98{,}7$ cm/s² di $s=\pm10$ cm ($t=0;\,1;\,2;\,3;\,4$); laju nol.

@@ P54 | Latihan 54 | Dua massa pada pegas | gerak | 287
$s_1=2\sin t$, $s_2=\sin2t$. (a) Kapan kedua massa berpapasan ($t>0$)? (b) Kapan jarak vertikalnya terbesar pada $[0;\,2\pi]$ dan berapa?

{{fig:h_p54}}
===
(a) $2\sin t=2\sin t\cos t\Rightarrow\sin t(1-\cos t)=0\Rightarrow t=\pi,2\pi,3\pi,\dots$

(b) $f=\sin2t-2\sin t$, $f'=2(2\cos^2t-\cos t-1)=0\Rightarrow t=\dfrac{2\pi}{3},\dfrac{4\pi}{3}$.

**Jawab:** jarak maksimum $\dfrac{3\sqrt3}{2}\approx2{,}60$ m.

@@ P55 | Latihan 55 | Jarak dua kapal | lintasan | 287
Pukul 12.00 kapal $A$ berada 12 mil laut di utara kapal $B$. $A$ berlayar ke selatan 12 knot, $B$ ke timur 8 knot. (a) Nyatakan jarak $s(t)$. (b) Laju perubahan jarak pukul 12.00 dan 13.00. (c) Jarak pandang 5 mil laut: apakah mereka saling terlihat? (d) Gambarkan grafik $s$ dan $ds/dt$. (e) Limit $ds/dt$.

{{fig:h_p55}}
===
(a) $s(t)=\sqrt{(12-12t)^2+64t^2}$.

(b) $s'=\dfrac{208t-144}{s}$: $s'(0)=-12$ knot, $s'(1)=8$ knot.

(c) Minimum di $t=\tfrac9{13}$ jam: $s\approx6{,}66>5$. Tidak pernah saling terlihat.

(d)

{{fig:h_p55g}}

$s'$ memotong nol tepat saat $s$ minimum.

(e) $\lim s'=\sqrt{208}=\sqrt{12^2+8^2}\approx14{,}4$ knot, yaitu resultan kedua kecepatan.

@@ P56 | Latihan 56 | Hukum pemantulan dari Prinsip Fermat | lintasan | 287
Cahaya dari $A$ dipantulkan cermin datar menuju $B$. Buktikan sudut datang sama dengan sudut pantul.

{{fig:h_p56}}
===
$A=(0,a)$, $B=(d,b)$, titik pantul $(x,0)$:

$$L(x)=\sqrt{x^2+a^2}+\sqrt{(d-x)^2+b^2}.$$

$$L'=\frac{x}{\sqrt{x^2+a^2}}-\frac{d-x}{\sqrt{(d-x)^2+b^2}}=\sin\theta_1-\sin\theta_2=0.$$

$L''>0$, jadi minimum; karena $\theta_1,\theta_2$ lancip, $\theta_1=\theta_2$. $\blacksquare$

@@ P58 | Latihan 58 | Lintasan pendaratan polinomial kubik | struktur | 287
Pesawat mulai turun dari ketinggian $H$ pada jarak horizontal $L$ dari bandara. Lintasan $y=ax^3+bx^2+cx+d$ dengan $y(-L)=H$, $y(0)=0$. (a)–(b) Berapa $dy/dx$ di $x=0$ dan $x=-L$? (c) Tunjukkan $y=H\left[2\left(\dfrac xL\right)^3+3\left(\dfrac xL\right)^2\right]$.

{{fig:h_p58}}
===
(a)–(b) Terbang datar dan mendarat mulus: kedua turunan **nol**.

(c) $y(0)=0\Rightarrow d=0$; $y'(0)=0\Rightarrow c=0$. $y'(-L)=3aL^2-2bL=0\Rightarrow b=\tfrac32aL$. $y(-L)=-aL^3+bL^2=H\Rightarrow a=\dfrac{2H}{L^3}$, $b=\dfrac{3H}{L^2}$. Substitusi menghasilkan rumus yang diminta. $\blacksquare$

Teknik yang sama dipakai untuk kurva transisi vertikal pada geometrik jalan.

@@ P61 | Latihan 61 | Rumus ukuran pesanan ekonomis (Wilson) | biaya | 288
Biaya mingguan persediaan $A(q)=\dfrac{km}{q}+cm+\dfrac{hq}{2}$. (a) $q$ yang meminimumkan $A$? (b) Jika ongkos pesan menjadi $k+bq$, berapa $q$ optimum?
===
(a) $A'=-\dfrac{km}{q^2}+\dfrac h2=0\Rightarrow q=\sqrt{\dfrac{2km}{h}}$ ($A''>0$).

(b) $A=\dfrac{km}{q}+bm+cm+\dfrac{hq}{2}$; suku $bm$ konstan, sehingga **$q$ optimum tetap** $\sqrt{2km/h}$.

@@ P65 | Latihan 65 | Kotak terbuka berbiaya minimum | biaya | 288
Kotak terbuka beralas persegi bervolume $6\ \text{m}^3$. Biaya alas 60 dolar/m², dinding 40 dolar/m². Tentukan dimensi dan biaya minimum.
===
$h=6/x^2$, $C=60x^2+160xh=60x^2+\dfrac{960}{x}$.

$C'=120x-\dfrac{960}{x^2}=0\Rightarrow x=2$.

**Jawab:** $2\times2\times1{,}5$ m, biaya $720$ dolar.

@@ P69 | Latihan 69 | Pertidaksamaan untuk bilangan bulat positif | dasar | 288
Buktikan untuk bilangan bulat positif $a,b,c,d$: $\dfrac{(a^2+1)(b^2+1)(c^2+1)(d^2+1)}{abcd}\ge16$.
===
Ruas kiri $=\prod\left(t+\dfrac1t\right)$. Fungsi $f(t)=t+1/t$ ($t>0$) minimum di $t=1$ dengan nilai $2$ (latihan 29). Jadi hasil kalinya $\ge2^4=16$. $\blacksquare$

@@ P70 | Latihan 70 | Sifat turunan waktu pada Hukum Snell | dasar | 288
Tunjukkan (a) $f(x)=\dfrac{x}{\sqrt{a^2+x^2}}$ naik; (b) $g(x)=\dfrac{d-x}{\sqrt{b^2+(d-x)^2}}$ turun; (c) $\dfrac{dt}{dx}=\dfrac{f(x)}{c_1}-\dfrac{g(x)}{c_2}$ naik.
===
(a) $f'=\dfrac{a^2}{(a^2+x^2)^{3/2}}>0$.

(b) $g'=-\dfrac{b^2}{(b^2+(d-x)^2)^{3/2}}<0$.

(c) $(dt/dx)'=\dfrac{f'}{c_1}-\dfrac{g'}{c_2}>0$. $\blacksquare$

@@ P71 | Latihan 71 | Jarak vertikal terbesar antara dua kurva | dasar | 288
Pada gambar, jarak vertikal $f$ dan $g$ terbesar di $x=c$. Apa keistimewaan garis singgung di titik itu?

{{fig:h_p71}}
===
$D=f-g$ maksimum di titik dalam $c$ dan terdiferensialkan, sehingga $D'(c)=0$, yaitu $f'(c)=g'(c)$.

**Jawab:** kedua garis singgung **sejajar**.

@@ P72 | Latihan 72 | Apakah fungsi trigonometri pernah negatif | dasar | 289
$f(x)=3+4\cos x+\cos2x$. (a) Mengapa cukup meninjau $[0;\,2\pi]$? (b) Pernahkah $f<0$?
===
(a) $f$ berperiode $2\pi$.

(b) $\cos2x=2\cos^2x-1$, sehingga $f=2(1+\cos x)^2\ge0$. **Tidak pernah negatif**; minimum $0$ di $x=\pi$.

@@ P73 | Latihan 73 | Maksimum mutlak kotangen dan kosekan | dasar | 289
(a) Tentukan maksimum mutlak $y=\cot x-\sqrt2\csc x$ pada $0<x<\pi$. (b) Bandingkan dengan grafik.
===
(a) $y'=\csc^2x(\sqrt2\cos x-1)=0\Rightarrow x=\pi/4$; tanda berubah $+$ ke $-$. Maksimum $y=-1$.

(b)

{{fig:h_p73}}

@@ P74 | Latihan 74 | Minimum mutlak tangen dan kotangen | dasar | 289
(a) Tentukan minimum mutlak $y=\tan x+3\cot x$ pada $0<x<\pi/2$. (b) Bandingkan dengan grafik.
===
(a) $y'=\sec^2x-3\csc^2x=0\Rightarrow\tan^2x=3\Rightarrow x=\pi/3$. Minimum $y=2\sqrt3\approx3{,}46$.

(b)

{{fig:h_p74}}

@@ P75 | Latihan 75 | Jarak kurva akar ke sebuah titik | lintasan | 289
(a) Seberapa dekat kurva $y=\sqrt x$ ke titik $(3/2;\,0)$? (b) Gambarkan grafik fungsi jarak.

{{fig:h_p75}}
===
(a) $D^2=(x-\tfrac32)^2+x$, turunan $2x-2=0\Rightarrow x=1$. Jarak minimum $\dfrac{\sqrt5}{2}\approx1{,}12$.

(b)

{{fig:h_p75g}}

Minimum $D(x)$ di $x=1$.

@@ P76 | Latihan 76 | Jarak setengah lingkaran ke sebuah titik | lintasan | 289
(a) Seberapa dekat $y=\sqrt{16-x^2}$ ke titik $(1;\,\sqrt3)$? (b) Gambarkan grafik fungsi jarak.

{{fig:h_p76}}
===
(a) $D^2=(x-1)^2+(y-\sqrt3)^2=20-2x-2\sqrt3\,y$. Turunan nol saat $1+\sqrt3\,y'=0$ dengan $y'=-x/y$, jadi $y=\sqrt3x$, sehingga $x=2$.

**Jawab:** titik $(2;\,2\sqrt3)$, jarak minimum $2$.

(b)

{{fig:h_p76g}}
