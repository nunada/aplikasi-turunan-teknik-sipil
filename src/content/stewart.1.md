@@ C1 | Contoh 1 | Memagari lahan di tepi sungai | struktur | 337
Petani memiliki 1200 m pagar untuk lahan persegi panjang yang berbatasan dengan sungai lurus (sisi sungai tidak dipagari). Berapa dimensi lahan terluas?

{{fig:s_c1a s_c1b}}
===
Coba beberapa tata letak: lahan terlalu dangkal atau terlalu dalam menghasilkan luas kecil. Misalkan $x$ = kedalaman dan $y$ = lebar:

$$2x+y=1200,\qquad A(x)=x(1200-2x),\quad 0\le x\le600.$$

$$A'(x)=1200-4x=0\Rightarrow x=300.$$

$A(0)=0$, $A(300)=180\,000$, $A(600)=0$.

**Jawab:** dalam $300$ m dan lebar $600$ m (luas $180\,000\ \text{m}^2$).

@@ C2 | Contoh 2 | Kaleng minyak 1 liter berbiaya minimum | volume | 338
Kaleng silinder memuat 1 L. Tentukan dimensi yang meminimumkan logam yang dipakai.

{{fig:s_c2}}
===
$\pi r^2h=1000\Rightarrow h=\dfrac{1000}{\pi r^2}$. Luas seluruh logam:

$$A(r)=2\pi r^2+\frac{2000}{r},\qquad r>0.$$

$$A'(r)=\frac{4(\pi r^3-500)}{r^2}.$$

$A'<0$ di kiri dan $A'>0$ di kanan $r=\sqrt[3]{500/\pi}$, jadi titik itu minimum mutlak (uji turunan pertama).

**Jawab:** $r=\sqrt[3]{500/\pi}\approx5{,}42$ cm dan $h=2r\approx10{,}84$ cm.

**Cara implisit:** dari $A'=4\pi r+2\pi h+2\pi rh'=0$ dan $2rh+r^2h'=0$ diperoleh langsung $h=2r$.

@@ C3 | Contoh 3 | Titik pada parabola yang terdekat | lintasan | 339
Cari titik pada parabola $y^2=2x$ yang terdekat dengan $(1,4)$.

{{fig:s_c3}}
===
Titik pada parabola: $(y^2/2,\;y)$. Minimumkan kuadrat jaraknya:

$$f(y)=\left(\tfrac12y^2-1\right)^2+(y-4)^2,\qquad f'(y)=y^3-8.$$

$f'$ berubah dari negatif ke positif di $y=2$.

**Jawab:** titik $(2,2)$ dengan jarak $\sqrt5$.

@@ C4 | Contoh 4 | Menyeberangi sungai secepatnya | lintasan | 340
Dari titik $A$ di tepi sungai selebar 3 km, seseorang ingin ke $B$ di tepi seberang, 8 km ke hilir. Ia mendayung 6 km/jam dan berlari 8 km/jam (arus diabaikan). Di mana ia harus mendarat?

{{fig:s_c4}}
===
Titik darat $D$ berjarak $x$ dari $C$ (seberang $A$):

$$T(x)=\frac{\sqrt{x^2+9}}{6}+\frac{8-x}{8},\qquad 0\le x\le8.$$

$$T'=\frac{x}{6\sqrt{x^2+9}}-\frac18=0\iff4x=3\sqrt{x^2+9}\iff x=\frac{9}{\sqrt7}.$$

$T(0)=1{,}5$; $T(9/\sqrt7)=1+\sqrt7/8\approx1{,}33$; $T(8)\approx1{,}42$.

**Jawab:** mendarat sekitar $3{,}4$ km ke hilir dari $C$.

@@ C5 | Contoh 5 | Persegi panjang dalam setengah lingkaran berjari-jari r | geometri | 340–341
Cari luas persegi panjang terbesar di dalam setengah lingkaran berjari-jari $r$.

{{fig:s_c5a s_c5b}}
===
### Cara 1 (koordinat)

$A=2x\sqrt{r^2-x^2}$, $0\le x\le r$, dengan $A'=\dfrac{2(r^2-2x^2)}{\sqrt{r^2-x^2}}=0\Rightarrow x=\dfrac{r}{\sqrt2}$. Karena $A(0)=A(r)=0$, maksimumnya $A=r^2$.

### Cara 2 (sudut)

$A(\theta)=(2r\cos\theta)(r\sin\theta)=r^2\sin2\theta$, maksimum saat $\theta=\pi/4$.

**Jawab:** $A_{\max}=r^2$.

@@ P1 | Latihan 1 | Dua bilangan berjumlah 23 | dasar | 342
Cari dua bilangan berjumlah 23 dengan hasil kali maksimum: (a) perkirakan lewat tabel; (b) selesaikan dengan kalkulus.
===
(a)

| Bilangan 1 | Bilangan 2 | Hasil kali |
| 9 | 14 | 126 |
| 10 | 13 | 130 |
| 11 | 12 | 132 |
| 12 | 11 | 132 |
| 13 | 10 | 130 |

Maksimum tampak di antara 11 dan 12.

(b) $P=x(23-x)$, $P'=23-2x=0\Rightarrow x=11{,}5$.

**Jawab:** $11{,}5$ dan $11{,}5$ (hasil kali $132{,}25$).

@@ P2 | Latihan 2 | Selisih 100, hasil kali minimum | dasar | 342
Cari dua bilangan berselisih 100 dengan hasil kali minimum.
===
$P=x(x-100)$, $P'=2x-100=0\Rightarrow x=50$.

**Jawab:** $50$ dan $-50$ (hasil kali $-2500$).

@@ P3 | Latihan 3 | Hasil kali 100, jumlah minimum | dasar | 342
Cari dua bilangan positif dengan hasil kali 100 dan jumlah minimum.
===
$S=x+100/x$, $S'=1-100/x^2=0\Rightarrow x=10$; $S''>0$.

**Jawab:** $10$ dan $10$.

@@ P4 | Latihan 4 | Jumlah kuadrat minimum | dasar | 342
Jumlah dua bilangan positif 16. Berapa nilai terkecil jumlah kuadratnya?
===
$S=x^2+(16-x)^2$, $S'=4x-32=0\Rightarrow x=8$.

**Jawab:** $128$.

@@ P5 | Latihan 5 | Jarak vertikal maksimum garis dan parabola | dasar | 342
Berapa jarak vertikal maksimum antara $y=x+2$ dan $y=x^2$ untuk $-1\le x\le2$?
===
$D=x+2-x^2$, $D'=1-2x=0\Rightarrow x=\tfrac12$; $D(-1)=D(2)=0$.

**Jawab:** $\tfrac94$.

@@ P6 | Latihan 6 | Jarak vertikal minimum dua parabola | dasar | 342
Berapa jarak vertikal minimum antara $y=x^2+1$ dan $y=x-x^2$?
===
$D=2x^2-x+1>0$, $D'=4x-1=0\Rightarrow x=\tfrac14$.

**Jawab:** $\tfrac78$.

@@ P7 | Latihan 7 | Keliling tetap, luas maksimum | geometri | 342
Cari dimensi persegi panjang berkeliling 100 m dengan luas terbesar.
===
$A=x(50-x)$, $A'=50-2x=0\Rightarrow x=25$.

**Jawab:** $25\times25$ m.

@@ P8 | Latihan 8 | Luas tetap, keliling minimum | geometri | 342
Cari dimensi persegi panjang berluas $1000\ \text{m}^2$ dengan keliling terkecil.
===
$P=2x+2000/x$, $P'=2-2000/x^2=0\Rightarrow x=\sqrt{1000}$.

**Jawab:** persegi $10\sqrt{10}\times10\sqrt{10}$ m $\approx31{,}6$ m.

@@ P11 | Latihan 11 | Empat petak kandang dengan 300 m pagar | struktur | 342
Dengan 300 m pagar dibuat persegi panjang yang dibagi menjadi empat petak dengan pagar sejajar salah satu sisi. Berapa luas total terbesar? (Gambar kasus, susun model, selesaikan.)

{{fig:s_p11}}
===
Contoh coba-coba ($5x+2y=300$): $x=10$ memberi $1250$; $x=30$ memberi $2250$; $x=50$ memberi $1250\ \text{m}^2$.

Model: $A=xy$ dengan $y=150-2{,}5x$, $0\le x\le60$.

$$A'=150-5x=0\Rightarrow x=30,\;y=75.$$

**Jawab:** $2250\ \text{m}^2$.

@@ P12 | Latihan 12 | Kotak terbuka dari karton persegi 3 m | volume | 342–343
Kotak tanpa tutup dibuat dari karton persegi selebar 3 m dengan memotong persegi di keempat sudut. Cari volume terbesar.

{{fig:s_p12}}
===
Contoh: $x=0{,}25$ memberi $V\approx1{,}56$; $x=0{,}5$ memberi $2$; $x=1$ memberi $1\ \text{m}^3$.

Model: $V=x(3-2x)^2$, $0\le x\le1{,}5$.

$$V'=(3-2x)(3-6x)=0\Rightarrow x=0{,}5.$$

**Jawab:** $2\ \text{m}^3$ (alas $2\times2$ m, tinggi $0{,}5$ m).

@@ P13 | Latihan 13 | Lahan 15 000 m² dibagi dua | biaya | 343
Lahan persegi panjang $15\,000\ \text{m}^2$ dipagari dan dibagi dua dengan pagar sejajar salah satu sisi. Bagaimana agar biaya pagar minimum?
===
$xy=15\,000$, panjang pagar $F=3x+2y=3x+\dfrac{30\,000}{x}$.

$F'=3-\dfrac{30\,000}{x^2}=0\Rightarrow x=100$.

**Jawab:** $100\times150$ m dengan pembagi sejajar sisi 100 m; total pagar $600$ m.

@@ P14 | Latihan 14 | Lahan trapesium di tepi sungai | struktur | 343
Tersedia 400 m pagar untuk lahan trapesium di tepi sungai; satu sisi sejajar tiga kali sisi sejajar lainnya, sisi sungai tidak dipagari. Cari luas terbesar.

{{fig:s_p14}}
===
Sisi tegak $x$ dan $3x$, sisi alas $b=400-4x$ (tegak lurus keduanya):

$$A=\frac{x+3x}{2}(400-4x)=800x-8x^2.$$

$A'=800-16x=0\Rightarrow x=50$.

**Jawab:** $A_{\max}=20\,000\ \text{m}^2$ (sisi $50$, $150$, dan alas $200$ m).

@@ P15 | Latihan 15 | Lahan di samping lumbung dengan biaya terbatas | biaya | 343
Lahan persegi panjang menempel dinding utara lumbung (tanpa pagar di sana). Biaya pagar sisi barat dibagi dua dengan tetangga. Pagar 30 dolar/m dan anggaran petani 1800 dolar. Dimensi luas terbesar?

{{fig:s_p15}}
===
$L$ = panjang sisi selatan, $W$ = sisi timur/barat: $30\left(L+W+\tfrac W2\right)=1800\Rightarrow L=60-1{,}5W$.

$A=W(60-1{,}5W)$, $A'=60-3W=0\Rightarrow W=20$.

**Jawab:** $L=30$ m, $W=20$ m ($600\ \text{m}^2$).

@@ P16 | Latihan 16 | Biaya pagar minimum untuk 750 m² | biaya | 343
Pada latihan 15, jika ingin memagari $750\ \text{m}^2$, dimensi berapa yang meminimumkan biaya?
===
$C=30\left(\dfrac{750}{W}+1{,}5W\right)$, $C'=0\Rightarrow W^2=500$.

**Jawab:** $W=10\sqrt5\approx22{,}4$ m dan $L=15\sqrt5\approx33{,}5$ m.

@@ P17 | Latihan 17 | Persegi sebagai bentuk optimum | dasar | 343
Tunjukkan: (a) dengan luas tetap, keliling terkecil dimiliki persegi; (b) dengan keliling tetap, luas terbesar dimiliki persegi.
===
(a) $P=2x+2A/x$, $P'=2-2A/x^2=0\Rightarrow x=\sqrt A$; $P''>0$.

(b) Luas $x(P/2-x)$, turunan $P/2-2x=0\Rightarrow x=P/4$; fungsi cekung ke bawah.

Pada keduanya kedua sisi sama panjang. $\blacksquare$

@@ P18 | Latihan 18 | Kotak terbuka dengan bahan minimum | volume | 343
Kotak beralas persegi tanpa tutup bervolume $32\,000\ \text{cm}^3$. Cari dimensi dengan bahan minimum.
===
$S=x^2+4xh=x^2+\dfrac{128\,000}{x}$, $S'=0\Rightarrow x^3=64\,000$.

**Jawab:** $40\times40\times20$ cm.

@@ P19 | Latihan 19 | Volume terbesar dari 1200 cm² bahan | volume | 343
Tersedia $1200\ \text{cm}^2$ bahan untuk kotak beralas persegi tanpa tutup. Cari volume terbesar.
===
$x^2+4xh=1200$, $V=\dfrac{x(1200-x^2)}{4}$, $V'=\dfrac{1200-3x^2}{4}=0\Rightarrow x=20$.

**Jawab:** $V=4000\ \text{cm}^3$ ($h=10$ cm).

@@ P20 | Latihan 20 | Kotak dengan satu dinding berlapis dua | volume | 343
Kotak terbuka dibuat dari karton $2\times1$ m dengan memotong sudutnya. Salah satu dinding panjang berlapis ganda (sisinya dilipat dua kali). Cari volume terbesar.

{{fig:s_p20}}
===
Arah panjang: $2-2x$. Arah lebar terpakai satu lipatan bawah $x$ dan dua lipatan atas $2x$, sisa alas $1-3x$.

$$V=x(2-2x)(1-3x),\qquad0\le x\le\tfrac13.$$

$$V'=2(9x^2-8x+1)=0\Rightarrow x=\frac{4-\sqrt7}{9}\approx0{,}150.$$

**Jawab:** $V_{\max}\approx0{,}140\ \text{m}^3$.

@@ P21 | Latihan 21 | Wadah tanpa tutup berbiaya minimum | biaya | 343
Wadah persegi panjang tanpa tutup bervolume $10\ \text{m}^3$; panjang alas dua kali lebarnya. Alas 10 dolar/m², dinding 6 dolar/m². Berapa biaya termurah?
===
Lebar $w$, $h=\dfrac{5}{w^2}$:

$$C=10(2w^2)+6(6wh)=20w^2+\frac{180}{w}.$$

$C'=0\Rightarrow w^3=4{,}5$.

**Jawab:** $w\approx1{,}65$ m, $C_{\min}\approx163{,}54$ dolar.

@@ P22 | Latihan 22 | Wadah bertutup | biaya | 343
Ulangi latihan 21 jika wadah memiliki tutup dari bahan yang sama dengan dinding.
===
Tutup menambah $6(2w^2)=12w^2$: $C=32w^2+\dfrac{180}{w}$, $C'=0\Rightarrow w^3=\dfrac{45}{16}$.

**Jawab:** $w\approx1{,}41$ m, $C_{\min}\approx191{,}28$ dolar.

@@ P23 | Latihan 23 | Paket kotak berpenampang persegi | volume | 343
Paket pos dibatasi panjang + lingkar $\le274$ cm. Cari dimensi kotak beralas persegi bervolume terbesar.

{{fig:s_p23}}
===
$L=274-4x$, $V=x^2(274-4x)$, $V'=548x-12x^2=0\Rightarrow x=\dfrac{137}{3}$.

**Jawab:** penampang $\approx45{,}7\times45{,}7$ cm, panjang $\approx91{,}3$ cm.

@@ P24 | Latihan 24 | Tabung pos silinder | volume | 343
Dengan batas pada latihan 23, cari dimensi tabung silinder bervolume terbesar.
===
$L=274-2\pi r$, $V=\pi r^2(274-2\pi r)$, $V'=0\Rightarrow r=\dfrac{274}{3\pi}$.

**Jawab:** $r\approx29{,}1$ cm, $L\approx91{,}3$ cm.

@@ P25 | Latihan 25 | Titik garis terdekat ke titik asal | lintasan | 343
Cari titik pada garis $y=2x+3$ yang terdekat ke titik asal.
===
$D^2=x^2+(2x+3)^2$, turunan $10x+12=0$.

**Jawab:** $\left(-\tfrac65,\tfrac35\right)$.

@@ P26 | Latihan 26 | Titik kurva akar terdekat ke (3, 0) | lintasan | 343
Cari titik pada $y=\sqrt x$ yang terdekat ke $(3,0)$.
===
$D^2=(x-3)^2+x$, turunan $2x-5=0$.

**Jawab:** $\left(\tfrac52,\sqrt{5/2}\right)$.

@@ P27 | Latihan 27 | Titik elips terjauh | lintasan | 343
Cari titik pada elips $4x^2+y^2=4$ yang terjauh dari $(1,0)$.
===
$D^2=(x-1)^2+4-4x^2=-3x^2-2x+5$, $-1\le x\le1$. Turunan $-6x-2=0\Rightarrow x=-\tfrac13$.

**Jawab:** $\left(-\tfrac13,\pm\dfrac{4\sqrt2}{3}\right)$, jarak $\dfrac{4}{\sqrt3}$.

@@ P28 | Latihan 28 | Titik pada kurva sinus (numerik) | lintasan | 344
Tentukan, teliti dua desimal, titik pada $y=\sin x$ yang terdekat ke $(4,2)$.
===
$f=(x-4)^2+(\sin x-2)^2$. Titik kritis memenuhi

$$(x-4)+(\sin x-2)\cos x=0.$$

Metode Newton atau grafik memberi $x\approx2{,}65$.

**Jawab:** sekitar $(2{,}65;\;0{,}47)$.

@@ P29 | Latihan 29 | Persegi panjang dalam lingkaran | geometri | 344
Cari dimensi persegi panjang terluas di dalam lingkaran berjari-jari $r$.
===
Sudut $(x,y)$ dengan $x^2+y^2=r^2$: $A=4x\sqrt{r^2-x^2}$, $A'=0\Rightarrow x=r/\sqrt2=y$.

**Jawab:** persegi bersisi $\sqrt2\,r$.

@@ P30 | Latihan 30 | Persegi panjang dalam elips | geometri | 344
Cari luas persegi panjang terbesar di dalam elips $x^2/a^2+y^2/b^2=1$.
===
Parametrik $x=a\cos t$, $y=b\sin t$: $A=4xy=2ab\sin2t$, maksimum di $t=\pi/4$.

**Jawab:** $2ab$.

@@ P31 | Latihan 31 | Persegi panjang dalam segitiga sama sisi | geometri | 344
Cari dimensi persegi panjang terluas di dalam segitiga sama sisi bersisi $L$, satu sisinya pada alas.

{{fig:s_p31}}
===
Lebar $w$, tinggi $h=\dfrac{\sqrt3}{2}(L-w)$. $A=\dfrac{\sqrt3}{2}w(L-w)$, maksimum di $w=L/2$.

**Jawab:** $\dfrac L2\times\dfrac{\sqrt3L}{4}$.

@@ P32 | Latihan 32 | Trapesium dalam setengah lingkaran | geometri | 344
Cari luas trapesium terbesar di dalam lingkaran berjari-jari 1 dengan alas berupa diameter.

{{fig:s_p32}}
===
Sudut atas $(\pm\cos t,\sin t)$: $A=(1+\cos t)\sin t$.

$$A'=\cos t+\cos2t=0\Rightarrow t=\frac\pi3.$$

**Jawab:** $\dfrac{3\sqrt3}{4}$.

@@ P33 | Latihan 33 | Segitiga sama kaki dalam lingkaran | geometri | 344
Cari dimensi segitiga sama kaki terluas di dalam lingkaran berjari-jari $r$.
===
Alas berada $y$ di bawah pusat: $A=\sqrt{r^2-y^2}\,(r+y)$. $A'=0\iff r^2-ry-2y^2=0\Rightarrow y=r/2$.

**Jawab:** segitiga **sama sisi** (alas $\sqrt3r$, tinggi $\tfrac32r$).

@@ P34 | Latihan 34 | Sisi ketiga yang memaksimumkan luas | geometri | 344
Dua sisi sama dari segitiga sama kaki panjangnya $a$. Cari sisi ketiga agar luas maksimum.
===
$A=\tfrac12a^2\sin\theta$ maksimum saat $\theta=90^\circ$.

**Jawab:** $\sqrt2\,a$.

@@ P35 | Latihan 35 | Batas luas segitiga | geometri | 344
Satu sisi segitiga $a$ dan sisi lain $2a$. Tunjukkan luas terbesar yang mungkin $a^2$.
===
$A(\theta)=\tfrac12(a)(2a)\sin\theta=a^2\sin\theta$. $A'=a^2\cos\theta=0\Rightarrow\theta=\pi/2$, sehingga $A_{\max}=a^2$. $\blacksquare$

@@ P36 | Latihan 36 | Persegi panjang di bawah parabola | geometri | 344
Alas persegi panjang pada sumbu-$x$ dan dua sudut atasnya pada $y=4-x^2$. Cari luas terbesar.
===
$A=2x(4-x^2)$, $A'=8-6x^2=0\Rightarrow x=\dfrac{2}{\sqrt3}$.

**Jawab:** $\dfrac{32}{3\sqrt3}\approx6{,}16$.

@@ P37 | Latihan 37 | Silinder dalam bola | volume | 344
Cari volume terbesar silinder tegak di dalam bola berjari-jari $r$.

{{fig:s_p37}}
===
Tinggi $2y$, jari-jari$^2=r^2-y^2$: $V=2\pi y(r^2-y^2)$, $V'=0\Rightarrow y=r/\sqrt3$.

**Jawab:** $\dfrac{4\pi r^3}{3\sqrt3}$.

@@ P38 | Latihan 38 | Silinder dalam kerucut | volume | 344
Silinder tegak di dalam kerucut berjari-jari $r$ dan tinggi $h$. Cari volume terbesar.

{{fig:s_p38}}
===
Jari-jari silinder $x$, tingginya $h(1-x/r)$: $V=\pi hx^2\left(1-\dfrac xr\right)$, $V'=0\Rightarrow x=\dfrac{2r}{3}$.

**Jawab:** $\dfrac{4\pi r^2h}{27}$.

@@ P39 | Latihan 39 | Luas permukaan silinder dalam bola | volume | 344
Cari luas permukaan terbesar silinder tegak di dalam bola berjari-jari $r$.
===
Jari-jari $r\cos\theta$, tinggi $2r\sin\theta$:

$$S=2\pi r^2\cos^2\theta+4\pi r^2\sin\theta\cos\theta=\pi r^2(1+\cos2\theta+2\sin2\theta).$$

$S'=0\Rightarrow\tan2\theta=2$.

**Jawab:** $S_{\max}=\pi r^2(1+\sqrt5)$.

@@ P40 | Latihan 40 | Jendela Norman | struktur | 344
Jendela Norman (persegi panjang ditambah setengah lingkaran selebar jendela) berkeliling 10 m. Cari dimensi yang memasukkan cahaya terbanyak.

{{fig:s_p40}}
===
$2r+2h+\pi r=10$. Luas:

$$A=2rh+\frac{\pi r^2}{2}=10r-2r^2-\frac{\pi r^2}{2}.$$

$A'=10-(4+\pi)r=0\Rightarrow r=\dfrac{10}{4+\pi}$ dan $h=r$.

**Jawab:** lebar $\dfrac{20}{4+\pi}\approx2{,}80$ m, tinggi persegi panjang $\approx1{,}40$ m.

@@ P41 | Latihan 41 | Poster terkecil | geometri | 344
Margin atas dan bawah poster 6 cm, margin samping 4 cm, area cetak $384\ \text{cm}^2$. Cari poster terkecil.

{{fig:s_p41}}
===
Area cetak $x\times384/x$: $A=(x+8)\left(\dfrac{384}{x}+12\right)$, $A'=12-\dfrac{3072}{x^2}=0\Rightarrow x=16$.

**Jawab:** poster $24\times36$ cm.

@@ P42 | Latihan 42 | Area cetak terbesar | geometri | 344
Poster berluas $900\ \text{cm}^2$ bermargin 2,5 cm di bawah dan samping serta 5 cm di atas. Dimensi berapa yang memaksimumkan area cetak?
===
Lebar $x$, tinggi $900/x$: $A=(x-5)\left(\dfrac{900}{x}-7{,}5\right)$, $A'=-7{,}5+\dfrac{4500}{x^2}=0\Rightarrow x=10\sqrt6$.

**Jawab:** lebar $\approx24{,}5$ cm, tinggi $\approx36{,}7$ cm.
