@@ C20 | Contoh 4.20 | Ekstrem mutlak pada interval tertutup | dasar | 275–276
Tentukan maksimum dan minimum mutlak $f(x)=\dfrac{x^3-2x^2+x+20}{x^2+5}$ pada $0\le x\le6$.

{{fig:t_c20}}
===
$f$ kontinu pada interval tertutup, jadi kedua ekstrem ada.

$$f'(x)=\frac{x^4+14x^2-60x+5}{(x^2+5)^2}=0\Rightarrow x\approx0{,}0850;\,2{,}7188.$$

| $x$ | 0 | 0,0850 | 2,7188 | 6 |
| $f(x)$ | 4 | 4,008 | 2,262 | 4,146 |

**Jawab:** minimum $2{,}262$ dan maksimum $4{,}146$.

@@ C21 | Contoh 4.21 | Ekstrem pada interval tak hingga | dasar | 276–277
Tentukan ekstrem mutlak $f(x)=\dfrac{2x^2+3x}{x^2+4}$ pada (a) $x\ge5$ dan (b) $x\ge1$, jika ada.

{{fig:t_c21a t_c21b}}
===
$\lim_{x\to\infty}f=2$ (asimtot), dan

$$f'(x)=\frac{-(x-6)(3x+2)}{(x^2+4)^2}.$$

(a) Satu titik kritis $x=6$: maksimum $f(6)=\tfrac94$. Karena $f(5)=\tfrac{65}{29}>2$ dan $f\to2^+$, **minimum tidak ada** (nilai 2 tidak pernah tercapai).

(b) Maksimum tetap $\tfrac94$, minimum $f(1)=1$.

@@ C22 | Contoh 4.22 | Memagari lahan di tepi sungai | struktur | 277–278
Lahan persegi panjang dipagari tiga sisi dengan 1.000 m pagar (sisi keempat sungai). Tentukan panjang dan lebar lahan agar luasnya maksimum.

{{fig:t_c22}}
===
$2w+l=1.000$, sehingga $A(w)=1.000w-2w^2$, $0\le w\le500$.

$A'=1.000-4w=0\Rightarrow w=250$; $A(0)=A(500)=0$, $A(250)=125.000$.

**Jawab:** lebar $250$ m, panjang $500$ m.

@@ C23 | Contoh 4.23 | Kaleng minuman 300 mL | volume | 278–279
Kaleng silinder harus memuat 300 mL. Tentukan dimensi dengan luas permukaan minimum.

{{fig:t_c23a t_c23b}}
===
$A=2\pi r^2+2\pi rh$ dan $\pi r^2h=300$:

$$A(r)=2\pi r^2+\frac{600}{r},\qquad r>0.$$

$$A'(r)=4\pi r-\frac{600}{r^2}=0\Rightarrow r=\left(\frac{150}{\pi}\right)^{1/3}\approx3{,}63\text{ cm}.$$

$A\to\infty$ di kedua ujung domain, jadi ini minimum mutlak.

**Jawab:** $r\approx3{,}63$ cm, $h=2r\approx7{,}26$ cm.

@@ C24 | Contoh 4.24 | Debit maksimum pada pipa lingkaran | air | 279–280
Debit pipa lingkaran terisi sebagian: $Q=K(2R)^{5/2}\sqrt{\dfrac{(\theta-\sin\theta)^3}{\theta}}$, dengan $\theta$ sudut pusat keliling basah. Tentukan $\theta$ untuk debit maksimum (3 desimal).

{{fig:t_c24}}
===
Cukup maksimumkan $f(\theta)=\dfrac{(\theta-\sin\theta)^3}{\theta}$. Syarat $f'=0$ menyederhana menjadi

$$g(\theta)=2\theta-3\theta\cos\theta+\sin\theta=0.$$

Metode Newton dari $\theta_1=5$: $5{,}36955;\ 5{,}37849;\ 5{,}37851$.

**Jawab:** $\theta\approx5{,}379$ rad $\approx308^\circ$. Debit terbesar terjadi saat pipa **belum penuh**.

@@ C25 | Contoh 4.25 | Dari mercusuar ke pondok | lintasan | 280–281
Mercusuar 6 km dari pantai; pondok di pantai 9 km dari titik terdekat. Mendayung 3 km/jam, berjalan 5 km/jam. Di mana harus mendarat? Ulangi jika pondok hanya 4 km.

{{fig:t_c25}}
===
$$t(x)=\frac{\sqrt{x^2+36}}{3}+\frac{9-x}{5},\qquad0\le x\le9.$$

$$t'=\frac{x}{3\sqrt{x^2+36}}-\frac15=0\Rightarrow25x^2=9(x^2+36)\Rightarrow x=4{,}5.$$

$t(0)=3{,}8$; $t(4{,}5)=3{,}4$; $t(9)\approx3{,}6$ jam. Mendarat $4{,}5$ km dari pondok.

Jika pondok 4 km: $x=4{,}5$ di luar $[0;\,4]$. $t(0)=2{,}8$ dan $t(4)\approx2{,}40$, jadi **dayung langsung ke pondok**.

@@ C26 | Contoh 4.26 | Balok terkuat dari gelondongan | struktur | 282
Kekuatan balok persegi panjang sebanding dengan lebar kali kuadrat tinggi. Tentukan dimensi balok terkuat dari gelondongan berjari-jari $R$.

{{fig:t_c26a t_c26b}}
===
$S=kwd^2$ dan $d^2=4R^2-w^2$:

$$S=kw(4R^2-w^2),\quad\frac{dS}{dw}=k(4R^2-3w^2)=0\Rightarrow w=\frac{2R}{\sqrt3}.$$

$S(0)=S(2R)=0$.

**Jawab:** $w=\dfrac{2R}{\sqrt3}$, $d=\dfrac{2\sqrt2R}{\sqrt3}$.

@@ C27 | Contoh 4.27 | Balok penopang melewati tembok | struktur | 282–283
Dinding gedung ditopang balok berpenampang $10\times10$ cm yang melewati tembok setinggi 5 m berjarak 2 m dari gedung. Balok menempel di gedung dan di lantai. Tentukan panjang balok terpendek.

{{fig:t_c27}}
===
Dengan $\theta$ sudut terhadap lantai:

$$D(\theta)=(2+5\cot\theta)\sec\theta+\frac1{10}(\cot\theta+\tan\theta),\qquad0<\theta<\frac\pi2.$$

$D'=0$ menjadi $20\sin^3\theta-50\cos^3\theta+2\sin^2\theta-1=0$. Metode Newton dari $\theta=1$ memberi $\theta\approx0{,}9314$.

**Jawab:** panjang minimum $\approx9{,}8$ m.

@@ C28 | Contoh 4.28 | Offset engkol untuk langkah maksimum | struktur | 284
Pada mekanisme engkol-peluncur (jari-jari $r$, batang $L$, offset $e\le r$), tentukan offset yang memaksimumkan panjang langkah.

{{fig:t_c28}}
===
Selisih posisi titik mati luar dan dalam:

$$s(e)=\sqrt{(L+r)^2-e^2}-\sqrt{(L-r)^2-e^2}.$$

$$s'(e)=e\left(\frac{1}{\sqrt{(L-r)^2-e^2}}-\frac{1}{\sqrt{(L+r)^2-e^2}}\right)>0\quad(e>0).$$

Fungsi naik, tidak ada titik kritis di dalam interval.

**Jawab:** $e=r$.

@@ L5 | Proyek Konsultasi 5 | Kedalaman batuan dasar dengan sinyal seismik | lintasan | 285–287
Lapisan tanah setebal $D$ berada di atas batuan. Sumber di $A$ memancarkan sinyal; penerima di $B$ berjarak $s$. Laju di tanah $v_1$ (terukur), di batuan $v_2>v_1$ (tidak diketahui). Tentukan $D$.

{{fig:t_l5a t_l5b}}
===
Hanya sinyal yang **tiba pertama** yang dapat dikenali. Lintasan tercepat simetris dengan sudut $\theta$ di kedua ujung:

$$t(\theta)=\frac{2D}{v_1}\csc\theta+\frac{s-2D\cot\theta}{v_2},\qquad\arctan\frac{2D}{s}\le\theta\le\frac\pi2.$$

$$t'(\theta)=\frac{-2D}{v_1v_2\sin^2\theta}(v_2\cos\theta-v_1)=0\Rightarrow\cos\theta=\frac{v_1}{v_2}.$$

Waktu minimumnya

$$\bar t=\frac{2D}{v_1}\sqrt{1-\left(\frac{v_1}{v_2}\right)^2}+\frac{s}{v_2}.$$

Ini garis lurus $\bar t=ms+b$. Ukur beberapa pasangan $(s_i,\bar t_i)$ **pada jarak yang cukup jauh sehingga gelombang refraksi tiba lebih dahulu** (pada jarak pendek, gelombang langsung di lapisan tanah dapat tiba lebih dahulu), tarik garis terbaik, lalu

$$v_2=\frac1m,\qquad D=\frac{b\,v_1}{2\sqrt{1-(v_1/v_2)^2}}.$$

{{fig:t_l5c}}

Inilah dasar metode **seismik refraksi** dalam penyelidikan tanah.

@@ P1 | Latihan 1 | Polinomial pada interval tertutup | dasar | 287
Tentukan ekstrem mutlak (tanpa grafik) $f(x)=x^3-x^2-5x+4$, $-2\le x\le3$.
===
$f'=(3x-5)(x+1)$. Nilai: $f(-2)=2$, $f(-1)=7$, $f(5/3)=-\tfrac{67}{27}$, $f(3)=7$.

**Jawab:** maksimum $7$, minimum $-\tfrac{67}{27}$.

@@ P2 | Latihan 2 | Fungsi rasional monoton | dasar | 287
Tentukan ekstrem mutlak $f(x)=\dfrac{x-4}{x+1}$, $0\le x\le10$.
===
$f'=\dfrac{5}{(x+1)^2}>0$, jadi fungsi naik.

**Jawab:** minimum $f(0)=-4$, maksimum $f(10)=\tfrac6{11}$.

@@ P3 | Latihan 3 | Jumlah dengan kebalikan | dasar | 287
Tentukan ekstrem mutlak $f(x)=x+\dfrac1x$, $\tfrac12\le x\le5$.
===
$f'=1-1/x^2=0\Rightarrow x=1$. $f(\tfrac12)=2{,}5$, $f(1)=2$, $f(5)=5{,}2$.

**Jawab:** minimum $2$, maksimum $\tfrac{26}{5}$.

@@ P4 | Latihan 4 | Fungsi trigonometri | dasar | 287
Tentukan ekstrem mutlak $f(x)=x-2\sin x$, $0\le x\le4\pi$.
===
$f'=1-2\cos x=0\Rightarrow x=\dfrac\pi3;\,\dfrac{5\pi}3;\,\dfrac{7\pi}3;\,\dfrac{11\pi}3$. Bandingkan juga $f(0)=0$ dan $f(4\pi)=4\pi$.

**Jawab:** minimum $\dfrac\pi3-\sqrt3\approx-0{,}685$; maksimum $\dfrac{11\pi}{3}+\sqrt3\approx13{,}25$.

@@ P5 | Latihan 5 | Fungsi akar | dasar | 287
Tentukan ekstrem mutlak $f(x)=x\sqrt{x+1}$, $-1\le x\le1$.
===
$f'=\dfrac{3x+2}{2\sqrt{x+1}}=0\Rightarrow x=-\tfrac23$. $f(-1)=0$, $f(1)=\sqrt2$.

**Jawab:** minimum $-\dfrac{2\sqrt3}{9}$, maksimum $\sqrt2$.

@@ P6 | Latihan 6 | Interval setengah garis | dasar | 287
Tentukan ekstrem mutlak $f(x)=\dfrac{12}{x^2+2x+2}$, $x<0$.
===
Penyebut $(x+1)^2+1$ minimum di $x=-1$.

**Jawab:** maksimum $12$; minimum tidak ada ($f\to0$ saat $x\to-\infty$ tetapi tidak tercapai).

@@ P7 | Latihan 7 | Tanpa ekstrem | dasar | 287
Tentukan ekstrem mutlak $f(x)=\dfrac{x+1}{x-1}$, $x>1$.
===
$f'=\dfrac{-2}{(x-1)^2}<0$; $f\to\infty$ saat $x\to1^+$ dan $f\to1$ saat $x\to\infty$.

**Jawab:** tidak ada maksimum maupun minimum mutlak.

@@ P8 | Latihan 8 | Satu maksimum | dasar | 287
Tentukan ekstrem mutlak $f(x)=\dfrac{x}{x^2+3}$, $x>0$.
===
$f'=\dfrac{3-x^2}{(x^2+3)^2}=0\Rightarrow x=\sqrt3$.

**Jawab:** maksimum $\dfrac{\sqrt3}{6}$; minimum tidak ada.

@@ P9 | Latihan 9 | Rasional dengan asimtot | dasar | 287
Tentukan ekstrem mutlak $f(x)=\dfrac{(2x-1)(x-8)}{(x-1)(x-4)}$, $x\le-2$.
===
$$f'=\frac{7x^2-28}{(x^2-5x+4)^2}\ge0\quad\text{untuk }x\le-2.$$

$f$ naik dari asimtot $y=2$.

**Jawab:** maksimum $f(-2)=\tfrac{25}{9}$; minimum tidak ada.

@@ P10 | Latihan 10 | Pembuktian dengan teorema nilai ekstrem | dasar | 287
Gunakan Teorema 4.2 (fungsi kontinu pada interval tertutup mencapai ekstrem mutlak) untuk membuktikan Teorema 3.17 pada §3.14.
===
**Teorema 3.17 (Teorema Rolle), §3.14, hlm. 229:** jika $f$ kontinu pada $[a,b]$, terdiferensialkan pada $(a,b)$, dan $f(a)=f(b)$, maka ada $c\in(a,b)$ dengan $f'(c)=0$.

**Bukti.** Menurut Teorema 4.2, $f$ mencapai maksimum $M$ dan minimum $m$. Jika $M=m$, $f$ konstan sehingga $f'=0$ di mana saja. Jika $M>m$, setidaknya satu ekstrem berbeda dari $f(a)=f(b)$, sehingga tercapai di titik dalam $c$. Di ekstrem dalam yang terdiferensialkan, $f'(c)=0$. $\blacksquare$

@@ P11 | Latihan 11 | Lendutan maksimum balok jepit-sendi | struktur | 287
Balok seragam panjang $L$ terjepit di satu ujung dan bertumpu sederhana di ujung lain:

$$(48EI)\,y=-mg(2x^4-5Lx^3+3L^2x^2).$$

Seberapa jauh dari jepitan lendutan maksimum terjadi?

{{fig:t_p11}}
===
Maksimumkan $g(x)=2x^4-5Lx^3+3L^2x^2$ pada $[0,L]$:

$$g'(x)=x(8x^2-15Lx+6L^2)=0\Rightarrow x=\frac{15-\sqrt{33}}{16}L.$$

Akar lain lebih besar dari $L$, dan $g(0)=g(L)=0$.

**Jawab:** $x\approx0{,}578L$ dari ujung terjepit.

@@ P12 | Latihan 12 | Pagar delapan petak percobaan | biaya | 287
Delapan petak persegi panjang berderet (seperti gambar), masing-masing $9.000\ \text{m}^2$. Tentukan panjang pagar minimum.

{{fig:t_p12}}
===
Petak $x\times y$: ada 9 pagar tegak dan 16 ruas mendatar, $F=16x+9y=16x+\dfrac{81.000}{x}$.

$F'=0\Rightarrow x=\sqrt{5.062{,}5}\approx71{,}15$, $y\approx126{,}5$.

**Jawab:** $F_{\min}\approx2.277$ m.

@@ P13 | Latihan 13 | Kotak tertutup dengan luas tetap | volume | 287
Kotak tertutup berpanjang tiga kali lebar dan berluas permukaan $30\ \text{m}^2$. Tentukan dimensi kotak agar volumenya maksimum.
===
Lebar $w$: $6w^2+8wh=30$, $V=3w^2h=\dfrac{90w-18w^3}{8}$. $V'=0\Rightarrow w^2=\tfrac53$.

**Jawab:** lebar $\approx1{,}29$ m, panjang $\approx3{,}87$ m, tinggi $\approx1{,}94$ m.

@@ P14 | Latihan 14 | Bak 6.000 liter beralas persegi | volume | 287
Kotak terbuka beralas persegi bervolume 6.000 L. Tentukan dimensi dengan bahan minimum.
===
$V=6\ \text{m}^3$, $S=x^2+\dfrac{24}{x}$, $S'=0\Rightarrow x^3=12$.

**Jawab:** alas $\sqrt[3]{12}\approx2{,}29$ m, tinggi $\approx1{,}14$ m.

@@ P16 | Latihan 16 | Lapangan di dalam lintasan 400 m | geometri | 287
Lintasan 400 m berjalan sepanjang lapangan dengan setengah lingkaran (diameter = lebar lapangan) di luar zona akhir sedalam 10 m. Tentukan dimensi yang memaksimumkan area permainan.

{{fig:t_p16}}
===
Panjang area permainan $l$, lebar $w$: $2(l+20)+\pi w=400\Rightarrow l=180-\dfrac{\pi w}{2}$.

$A=lw=180w-\dfrac{\pi w^2}{2}$, $A'=0\Rightarrow w=\dfrac{180}{\pi}$.

**Jawab:** lebar $\approx57{,}3$ m, panjang $90$ m.

@@ P18 | Latihan 18 | Persegi panjang dalam segitiga sama kaki | geometri | 287
Segitiga sama kaki beralas $b$ dan tinggi $a$. Tentukan luas persegi panjang terbesar dengan satu sisi pada alas.
===
Tinggi persegi panjang $y$, lebar $b(1-y/a)$: $A=by(1-y/a)$, maksimum di $y=a/2$.

**Jawab:** $\dfrac{ab}{4}$.

@@ P19 | Latihan 19 | Kaleng 1.000 cm³ dengan sisa potongan | volume | 288
Kaleng $1.000\ \text{cm}^3$; tiap tutup dipotong dari pelat persegi (sisanya terbuang). Tentukan tinggi dan jari-jari dengan logam minimum termasuk sisa.
===
$A=8r^2+\dfrac{2.000}{r}$, $A'=0\Rightarrow r=5$.

**Jawab:** $r=5$ cm, $h=\dfrac{40}{\pi}\approx12{,}7$ cm.

@@ P20 | Latihan 20 | Titik dengan jumlah jarak minimum | struktur | 288
Segitiga sama kaki $ABC$ ($AB=AC$) beralas $BC=2a$ dengan tinggi $AD=2a$. Tentukan tinggi titik $P$ pada $AD$ agar $AP+BP+CP$ minimum.

{{fig:t_p20}}
===
$PD=y$: $S=(2a-y)+2\sqrt{a^2+y^2}$.

$S'=-1+\dfrac{2y}{\sqrt{a^2+y^2}}=0\Rightarrow y=\dfrac{a}{\sqrt3}$.

**Jawab:** $\dfrac{a}{\sqrt3}$ di atas alas (ketiga ruas membentuk sudut $120^\circ$).

@@ P21 | Latihan 21 | Tali terpendek pada dua tiang | struktur | 288
Dua tiang berjarak 3 m setinggi 2 m dan 1 m. Seutas tali dari puncak ke puncak melalui pengait di tanah. Di mana pengait agar tali terpendek?
===
$x$ dari tiang 2 m: $L=\sqrt{x^2+4}+\sqrt{(3-x)^2+1}$. $L'=0$ saat kemiringan kedua ruas sama: $\dfrac x2=\dfrac{3-x}{1}$.

**Jawab:** $2$ m dari tiang yang tinggi ($L=3\sqrt2$ m).

@@ P22 | Latihan 22 | Halaman buku terkecil | geometri | 288
Area cetak halaman $150\ \text{cm}^2$, margin samping 2,5 cm, margin atas-bawah 3,75 cm. Tentukan halaman berluas terkecil.
===
$A=(x+5)\left(\dfrac{150}{x}+7{,}5\right)$, $A'=7{,}5-\dfrac{750}{x^2}=0\Rightarrow x=10$.

**Jawab:** halaman $15\times22{,}5$ cm.

@@ P23 | Latihan 23 | Titik hiperbola terdekat | lintasan | 288
Tentukan titik pada $y^2-x^2=9$ yang terdekat dengan $(4;\,0)$.
===
$D^2=(x-4)^2+x^2+9$, turunan $4x-8=0$.

**Jawab:** $(2,\pm\sqrt{13})$.

@@ P24 | Latihan 24 | Titik parabola terdekat | lintasan | 288
Tentukan titik pada $y=x^2$ yang terdekat dengan $(-2;\,5)$.
===
$D^2=(x+2)^2+(x^2-5)^2$, turunan $2(2x^3-9x+2)=2(x-2)(2x^2+4x-1)=0$.

Akar: $2$, $-1\pm\dfrac{\sqrt6}{2}$. Nilai $D^2$ terkecil di $x=-1-\dfrac{\sqrt6}{2}\approx-2{,}225$.

**Jawab:** sekitar $(-2{,}225;\;4{,}949)$.

@@ P25 | Latihan 25 | Tinggi lampu untuk penerangan tepi maksimum | struktur | 288
Lampu di atas pusat daerah lingkaran berjari-jari $r$. Penerangan di tepi sebanding dengan $\cos\theta$ dan berbanding terbalik dengan $d^2$. Tinggi $h$ berapa yang optimum?

{{fig:t_p25}}
===
$$I=\frac{k\cos\theta}{d^2}=\frac{kh}{(r^2+h^2)^{3/2}},\quad I'\propto r^2-2h^2=0.$$

**Jawab:** $h=\dfrac{r}{\sqrt2}$.

@@ P26 | Latihan 26 | Segitiga terkecil melalui titik (2, 5) | geometri | 288
Dari semua ruas garis antara sumbu positif yang melalui $(2;\,5)$, tentukan yang membentuk segitiga terkecil.
===
$\dfrac2a+\dfrac5b=1$, $A=\dfrac{5a^2}{2(a-2)}$, $A'=0\Rightarrow a=4$, $b=10$.

**Jawab:** ruas dari $(4;\,0)$ ke $(0;\,10)$; luas $20$.

@@ P27 | Latihan 27 | Saluran pelimpah trapesium | air | 288
Lembaran logam selebar 1 m ditekuk dua kali menjadi saluran trapesium sama kaki dengan $AB=BC=CD=\tfrac13$ m. Sudut $\theta$ berapa memberi aliran maksimum?

{{fig:t_p27}}
===
$$A=\tfrac19\sin\theta\,(1+\cos\theta),\quad A'=\tfrac19(\cos\theta+\cos2\theta)=0.$$

**Jawab:** $\theta=\dfrac\pi3$.

@@ P31 | Latihan 31 | Dua kapal terdekat | lintasan | 288
Pukul 12.00 kapal $S_1$ 20 km di utara $S_2$. $S_1$ ke selatan 6 km/jam, $S_2$ ke timur 8 km/jam. Kapan jaraknya minimum?
===
$D^2=(20-6t)^2+64t^2$, turunan $-12(20-6t)+128t=0\Rightarrow t=1{,}2$ jam.

**Jawab:** pukul 13.12 (jarak $16$ km).

@@ P32 | Latihan 32 | Kurir melintasi gurun | lintasan | 288
Kurir berada 6 km dari titik $P$ (titik terdekat di jalan). Laju di gurun 14 km/jam, di jalan 50 km/jam. Di mana ia masuk jalan bila tujuan $Q$ berjarak (a) 3 km, (b) 1 km dari $P$?
===
$T=\dfrac{\sqrt{36+x^2}}{14}+\dfrac{d-x}{50}$, $T'=0\Rightarrow50x=14\sqrt{36+x^2}\Rightarrow x=1{,}75$.

(a) Masuk jalan $1{,}75$ km dari $P$ ke arah $Q$.

(b) $1{,}75>1$, dan $T$ turun pada $[0;\,1]$: **langsung menuju $Q$**.

@@ P33 | Latihan 33 | Persegi panjang dalam lingkaran | geometri | 288
Tentukan luas persegi panjang terbesar di dalam lingkaran berjari-jari $r$.
===
$A=4r^2\sin t\cos t=2r^2\sin2t$.

**Jawab:** $2r^2$ (persegi).

@@ P34 | Latihan 34 | Persegi panjang terluas dalam elips | geometri | 288
Tentukan persegi panjang terluas di dalam elips $b^2x^2+a^2y^2=a^2b^2$ dengan sisi sejajar sumbu.
===
$x=a\cos t$, $y=b\sin t$: $A=2ab\sin2t$, maksimum di $t=\pi/4$.

**Jawab:** $\sqrt2a\times\sqrt2b$, luas $2ab$.

@@ P35 | Latihan 35 | Persegi panjang berkeliling terbesar dalam elips | geometri | 288
Pada elips yang sama, tentukan persegi panjang dengan keliling terbesar.
===
$P=4(a\cos t+b\sin t)$, $P'=0\Rightarrow\tan t=b/a$.

**Jawab:** sisi $\dfrac{2a^2}{\sqrt{a^2+b^2}}$ dan $\dfrac{2b^2}{\sqrt{a^2+b^2}}$; keliling $4\sqrt{a^2+b^2}$.

@@ P36 | Latihan 36 | Persegi panjang di bawah kurva lonceng | geometri | 288
Tentukan luas persegi panjang terbesar dengan satu sisi pada sumbu-$x$ dan dua sudut pada $y=e^{-x^2}$.
===
$A=2xe^{-x^2}$, $A'=2e^{-x^2}(1-2x^2)=0\Rightarrow x=\dfrac1{\sqrt2}$.

**Jawab:** $\sqrt{2/e}\approx0{,}858$.

@@ P37 | Latihan 37 | Silinder terbesar dalam bola | volume | 288
Tentukan volume silinder tegak terbesar di dalam bola berjari-jari $r$.
===
$V=\pi(r^2-y^2)(2y)$, $V'=0\Rightarrow y=r/\sqrt3$.

**Jawab:** $\dfrac{4\pi r^3}{3\sqrt3}$.

@@ P38 | Latihan 38 | Silinder terbesar dalam kerucut | volume | 288
Tentukan volume silinder tegak terbesar di dalam kerucut berjari-jari $r$ dan tinggi $h$.
===
$V=\pi x^2h(1-x/r)$, $V'=0\Rightarrow x=\tfrac{2r}{3}$.

**Jawab:** $\dfrac{4\pi r^2h}{27}$.

@@ P39 | Latihan 39 | Balok tambahan dari sisa gelondongan | struktur | 288
Setelah balok terkuat (Contoh 4.26) dipotong, dua balok lagi diambil dari sisa kayu yang lebih besar. Berapa dimensi balok terkuatnya?

{{fig:t_p39}}
===
Sisa terbesar ada di kiri dan kanan, di luar $x=\pm R/\sqrt3$. Ambil balok dari $x=R/\sqrt3$ sampai $X$: lebar $t=X-\dfrac R{\sqrt3}$ dan tinggi $u=2\sqrt{R^2-X^2}$.

$$S=ktu^2=4k\left(X-\tfrac{R}{\sqrt3}\right)(R^2-X^2),\quad S'=0\Rightarrow3X^2-\tfrac{2R}{\sqrt3}X-R^2=0.$$

$X=\dfrac{R(1+\sqrt{10})}{3\sqrt3}\approx0{,}801R$.

**Jawab:** lebar $\approx0{,}224R$, tinggi $\approx1{,}197R$.

@@ P40 | Latihan 40 | Sudut tolak peluru optimum | gerak | 289
Jangkauan peluru yang dilepas dari tinggi $h$ dengan laju $v$:

$$R=\frac{v^2\cos\theta}{g}\left(\sin\theta+\sqrt{\sin^2\theta+\frac{2gh}{v^2}}\right).$$

Tentukan $\theta$ optimum; hitung untuk $v=13{,}7$ m/s, $h=2{,}25$ m.

{{fig:t_p40}}
===
Dengan $s=\sin\theta$ dan $k=2gh/v^2$, kondisi $dR/d\theta=0$ menyederhana menjadi $s^2(2+k)=1$:

$$\sin\theta=\frac{v}{\sqrt{2v^2+2gh}}.$$

Untuk data tersebut ($g=9{,}81$): $\sin\theta\approx0{,}669$.

**Jawab:** $\theta\approx42{,}0^\circ$.
