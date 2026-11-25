@@ C1 | Contoh 1 | Kotak terbuka beralas persegi | volume | 219
Kotak tanpa tutup beralas persegi dibuat dari bahan seluas $108\ \text{inci}^2$. Tentukan dimensinya agar volume maksimum.

{{fig:lo_c1}}
===
$x^2+4xh=108$, sehingga $V=x^2h=27x-\dfrac{x^3}{4}$, $0\le x\le\sqrt{108}$.

$V'=27-\tfrac34x^2=0\Rightarrow x=6$. $V(0)=V(\sqrt{108})=0$, $V(6)=108$.

**Jawab:** $6\times6\times3$ inci.

@@ C2 | Contoh 2 | Titik parabola terdekat | lintasan | 221
Titik mana pada $y=4-x^2$ yang paling dekat ke $(0; 2)$?

{{fig:lo_c2}}
===
$d^2=x^2+(2-x^2)^2=x^4-3x^2+4=f(x)$, $f'=2x(2x^2-3)$. $x=0$ maksimum lokal, $x=\pm\sqrt{3/2}$ minimum.

**Jawab:** $\left(\pm\sqrt{3/2},\ \tfrac52\right)$.

@@ C3 | Contoh 3 | Halaman dengan margin | geometri | 221
Halaman memuat area cetak $24\ \text{inci}^2$ dengan margin atas-bawah $1\tfrac12$ inci dan samping 1 inci. Tentukan ukuran halaman agar kertas paling sedikit.

{{fig:lo_c3}}
===
Area cetak tinggi $x$, lebar $24/x$: $A=(x+3)\left(\dfrac{24}{x}+2\right)=30+2x+\dfrac{72}{x}$.

$A'=2-\dfrac{72}{x^2}=0\Rightarrow x=6$.

**Jawab:** tinggi 9 inci, lebar 6 inci.

@@ C4 | Contoh 4 | Kawat penahan dua tiang | struktur | 222
Dua tiang setinggi 12 ft dan 28 ft berjarak 30 ft diikat dengan kawat ke satu patok di tanah. Di mana patok dipasang agar kawat paling pendek?

{{fig:lo_c4}}
===
$$W=\sqrt{x^2+144}+\sqrt{(30-x)^2+784},\quad0\le x\le30.$$

$W'=0$ menghasilkan $320(x-9)(2x+45)=0$. $W(0)\approx53{,}0$; $W(9)=50$; $W(30)\approx60{,}3$.

**Jawab:** 9 ft dari tiang 12 ft.

@@ C5 | Contoh 5 | Maksimum di ujung interval | geometri | 223
Kawat 4 ft dipakai untuk persegi dan lingkaran (seluruh kawat boleh dipakai untuk satu bangun). Bagaimana pembagiannya agar total luas maksimum?

{{fig:lo_c5}}
===
Sisi persegi $x$, $r=\dfrac{2(1-x)}{\pi}$:

$$A=\frac1\pi\left[(\pi+4)x^2-8x+4\right],\quad0\le x\le1.$$

Titik kritis $x=\dfrac{4}{\pi+4}\approx0{,}56$ adalah minimum. $A(0)\approx1{,}27$, $A(1)=1$.

**Jawab:** seluruh kawat untuk lingkaran ($x=0$). Jika kedua bangun harus ada, maksimum tidak tercapai.

@@ P1 | Latihan 1 | Istilah optimisasi | dasar | 224
Definisikan persamaan utama, persamaan sekunder, dan domain layak.
===
- **Persamaan utama:** rumus besaran yang akan dioptimumkan.
- **Persamaan sekunder:** hubungan antarvariabel (kendala) untuk menjadikan persamaan utama fungsi satu variabel.
- **Domain layak:** nilai variabel yang masuk akal menurut soal.

@@ P2 | Latihan 2 | Panduan optimisasi | dasar | 224
Uraikan langkah menyelesaikan soal maksimum dan minimum terapan.
===
- Tentukan yang diketahui dan dicari; buat sketsa.
- Tulis persamaan utama.
- Reduksi menjadi satu variabel bebas dengan persamaan sekunder.
- Tentukan domain layak.
- Tentukan ekstrem dengan teknik kalkulus, periksa juga ujung interval.

@@ P3 | Latihan 3 | Dua bilangan berjumlah 110 | dasar | 224
Cara numerik, grafis, dan analitis: tentukan dua bilangan positif berjumlah 110 dengan hasil kali maksimum.
===
(a)

| $x$ | 10 | 20 | 30 | 40 | 50 | 60 |
| $P$ | 1.000 | 1.800 | 2.400 | 2.800 | 3.000 | 3.000 |

(b) $P=x(110-x)$. (c) $P'=110-2x=0\Rightarrow x=55$.

**Jawab:** 55 dan 55 ($P=3.025$). (d) Grafik di bawah.

@@ P4 | Latihan 4 | Kotak terbuka dari lembaran 24 inci | volume | 224
Kotak terbuka dibuat dari lembaran persegi 24 inci dengan memotong persegi di sudut. Selesaikan secara numerik dan analitis.

{{fig:lo_p4}}
===
(a)

| $x$ | 1 | 2 | 3 | 4 | 5 | 6 |
| $V$ | 484 | 800 | 972 | 1.024 | 980 | 864 |

(b) $V=x(24-2x)^2$, $0<x<12$. (c) $V'=(24-2x)(24-6x)=0\Rightarrow x=4$.

**Jawab:** $V_{\max}=1.024\ \text{inci}^3$.

@@ P5 | Latihan 5 | Jumlah tetap | dasar | 224
Dua bilangan positif berjumlah $S$ dengan hasil kali maksimum.
===
$P=x(S-x)$, $P'=0\Rightarrow x=S/2$. Keduanya $S/2$.

@@ P6 | Latihan 6 | Hasil kali 185 | dasar | 224
Hasil kali dua bilangan **positif** adalah 185. Tentukan kedua bilangan agar jumlahnya minimum.
===
$f=x+185/x$ dengan $x>0$, $f'=0\Rightarrow x=\sqrt{185}$ ($f''>0$). Keduanya $\sqrt{185}$.

@@ P7 | Latihan 7 | Hasil kali 147 | dasar | 224
Hasil kali dua bilangan **positif** adalah 147. Tentukan keduanya agar bilangan pertama ditambah tiga kali bilangan kedua minimum.
===
$b=147/a$ dengan $a>0$: $f=a+441/a$, $f'=0\Rightarrow a=21$, $b=7$.

@@ P8 | Latihan 8 | Kuadrat ditambah bilangan | dasar | 224
$a^2+b=54$ dan $ab$ maksimum ($a,b>0$).
===
$P=a(54-a^2)$, $P'=54-3a^2=0\Rightarrow a=3\sqrt2$, $b=36$.

@@ P9 | Latihan 9 | Satu ditambah dua kali | dasar | 224
Dua bilangan **positif** memenuhi $a+2b=108$. Tentukan keduanya agar $ab$ maksimum.
===
$P=b(108-2b)\Rightarrow b=27$, $a=54$.

@@ P10 | Latihan 10 | Pangkat tiga ditambah bilangan | dasar | 224
Dua bilangan **positif** memenuhi $a^3+b=500$. Tentukan keduanya agar $ab$ maksimum.
===
$P=a(500-a^3)$, $P'=500-4a^3=0\Rightarrow a=5$, $b=375$.

@@ P11 | Latihan 11 | Keliling 80 m | geometri | 224
Tentukan panjang dan lebar persegi panjang berkeliling 80 m agar luas maksimum.
===
$A=x(40-x)\Rightarrow x=20$: $20\times20$ m.

@@ P12 | Latihan 12 | Keliling P | geometri | 224
Persegi panjang berkeliling $P$ dengan luas maksimum.
===
$A=x(P/2-x)\Rightarrow x=P/4$: persegi bersisi $P/4$.

@@ P13 | Latihan 13 | Luas 49 | geometri | 224
Persegi panjang berluas $49\ \text{ft}^2$ dengan keliling minimum.
===
$2x+98/x$ minimum di $x=7$: $7\times7$ ft.

@@ P14 | Latihan 14 | Luas A | geometri | 224
Persegi panjang berluas $A$ dengan keliling minimum.
===
$2x+2A/x$ minimum di $x=\sqrt A$: persegi bersisi $\sqrt A$.

@@ P15 | Latihan 15 | Parabola dan titik (0, 3) | lintasan | 224
Titik pada $y=x^2$ terdekat ke $(0; 3)$.
===
$f=x^2+(x^2-3)^2$, $f'=2x(2x^2-5)$.

**Jawab:** $\left(\pm\sqrt{5/2},\ \tfrac52\right)$.

@@ P16 | Latihan 16 | Parabola dan titik (0, −1) | lintasan | 224
Titik pada $y=x^2-2$ terdekat ke $(0; -1)$.
===
$f=x^2+(x^2-1)^2$, $f'=2x(2x^2-1)$.

**Jawab:** $\left(\pm\tfrac{1}{\sqrt2},\ -\tfrac32\right)$.

@@ P17 | Latihan 17 | Kurva akar dan titik (4, 0) | lintasan | 224
Titik pada $f(x)=\sqrt x$ terdekat ke $(4; 0)$.
===
$(x-4)^2+x$ minimum di $x=\tfrac72$: $\left(\tfrac72,\ \sqrt{7/2}\right)$.

@@ P18 | Latihan 18 | Kurva akar dan titik (12, 0) | lintasan | 224
Titik pada $f(x)=\sqrt{x-8}$ terdekat ke $(12; 0)$.
===
$(x-12)^2+x-8$ minimum di $x=\tfrac{23}{2}$: $\left(\tfrac{23}{2},\ \sqrt{7/2}\right)$.

@@ P19 | Latihan 19 | Poster | geometri | 224
Area cetak $648\ \text{inci}^2$, margin atas-bawah 2 inci, samping 1 inci. Ukuran poster dengan kertas minimum?
===
Lebar cetak $w$: $A=(w+2)\left(\dfrac{648}{w}+4\right)$, $A'=4-\dfrac{1.296}{w^2}=0\Rightarrow w=18$.

**Jawab:** $20\times40$ inci.

@@ P20 | Latihan 20 | Halaman bermargin sama | geometri | 224
Area cetak $36\ \text{inci}^2$, margin tiap sisi $1\tfrac12$ inci. Ukuran halaman minimum?
===
$A=(w+3)\left(\dfrac{36}{w}+3\right)$, $A'=0\Rightarrow w=6$.

**Jawab:** $9\times9$ inci.

@@ P21 | Latihan 21 | Pagar padang rumput di tepi sungai | struktur | 224
Padang $405.000\ \text{m}^2$ di tepi sungai (sisi sungai tanpa pagar). Dimensi berapa yang meminimumkan pagar?

{{fig:lo_p21}}
===
$F=x+2y$, $x=405.000/y$: $F'=-\dfrac{405.000}{y^2}+2=0\Rightarrow y=450$.

**Jawab:** $x=900$ m dan $y=450$ m.

@@ P22 | Latihan 22 | Balok beralas persegi | volume | 225
Balok beralas persegi dengan luas permukaan $337{,}5\ \text{cm}^2$. Dimensi untuk volume maksimum?
===
$2x^2+4xh=337{,}5$, $V=\dfrac{x(337{,}5-2x^2)}{4}$, $V'=0\Rightarrow x=7{,}5$, $h=7{,}5$.

**Jawab:** kubus berusuk 7,5 cm.

@@ P23 | Latihan 23 | Jendela Norman | struktur | 225
Jendela persegi panjang beratap setengah lingkaran berkeliling 16 ft. Dimensi untuk luas maksimum?

{{fig:lo_p23}}
===
$x+2y+\dfrac{\pi x}{2}=16$, $A=xy+\dfrac{\pi x^2}{8}$. $A'=0\Rightarrow x=\dfrac{32}{4+\pi}$.

**Jawab:** lebar $\approx4{,}48$ ft, tinggi persegi panjang $\approx2{,}24$ ft.

@@ P24 | Latihan 24 | Persegi panjang di bawah garis | geometri | 225
Persegi panjang dibatasi sumbu koordinat dan $y=(6-x)/2$. Ukuran untuk luas maksimum?

{{fig:lo_p24}}
===
$A=x\dfrac{6-x}{2}\Rightarrow x=3$, $y=\tfrac32$.

@@ P25 | Latihan 25 | Garis melalui (1, 2) | geometri | 225
Segitiga siku-siku di kuadran I dibentuk garis melalui $(1; 2)$. (a) Nyatakan sisi miring $L$ dalam intersep-$x$. (b) Perkirakan $x$ untuk $L$ minimum. (c) Titik sudut untuk luas minimum.

{{fig:lo_p25}}
===
(a) Intersep-$y=\dfrac{2x}{x-1}$, $L=\sqrt{x^2+\dfrac{4x^2}{(x-1)^2}}$, $x>1$.

(b) Turunan nol saat $(x-1)^3=4$: $x=1+\sqrt[3]4\approx2{,}59$.

(c) $A=\dfrac{x^2}{x-1}$ minimum di $x=2$: titik $(0; 0)$, $(2; 0)$, $(0; 4)$.

@@ P26 | Latihan 26 | Segitiga sama kaki dalam lingkaran | geometri | 225
Tentukan luas segitiga sama kaki terbesar dalam lingkaran berjari-jari 6: (a) dengan $h$, (b) dengan $\alpha$, (c) jenis segitiganya.

{{fig:lo_p26}}
===
(a) $A=\sqrt{36-h^2}\thinspace (6+h)$, $A'=0\Rightarrow h=3$, $A=27\sqrt3$.

(b) $A=36\sin2\alpha\thinspace (1+\cos2\alpha)$, maksimum di $\alpha=30^\circ$.

(c) **Sama sisi.**

@@ P27 | Latihan 27 | Persegi panjang dalam setengah lingkaran 5 | geometri | 225
Persegi panjang dibatasi sumbu-$x$ dan $y=\sqrt{25-x^2}$. Ukuran untuk luas maksimum?

{{fig:lo_p27}}
===
$A=2x\sqrt{25-x^2}$, maksimum di $x=\dfrac{5}{\sqrt2}$.

**Jawab:** panjang $5\sqrt2$, lebar $\dfrac{5}{\sqrt2}$.

@@ P28 | Latihan 28 | Persegi panjang dalam setengah lingkaran r | geometri | 225
Ulangi latihan 27 untuk jari-jari $r$.
===
**Jawab:** $\sqrt2\thinspace r\times\dfrac{r}{\sqrt2}$.

@@ P29 | Latihan 29 | Ruang olahraga dan lintasan 200 m | geometri | 225
Ruang berbentuk persegi panjang dengan setengah lingkaran di dua ujung, dikelilingi lintasan 200 m. Selesaikan secara numerik dan analitis agar luas persegi panjang maksimum.

{{fig:lo_p29}}
===
(a)–(c) $2x+\pi y=200$, $A=\dfrac2\pi(100x-x^2)$.

| $x$ | 10 | 20 | 30 | 40 | 50 | 60 |
| $A$ | 573 | 1.019 | 1.337 | 1.528 | 1.592 | 1.528 |

(d) $A'=0\Rightarrow x=50$, $y=\dfrac{100}{\pi}\approx31{,}8$; $A=\dfrac{5.000}{\pi}\approx1.592\ \text{m}^2$. (e) Grafik di bawah.

@@ P30 | Latihan 30 | Kaleng 22 inci kubik | volume | 225
Silinder harus memuat $22\ \text{inci}^3$. Selesaikan secara numerik dan analitis untuk luas permukaan minimum.
===
(a)–(b)

| $r$ | 0,2 | 0,6 | 1,0 | 1,4 | 1,6 |
| $S$ | 220,3 | 75,6 | 50,3 | 43,7 | 43,6 |

(c) $S=2\pi r^2+\dfrac{44}{r}$. (d) $S'=0\Rightarrow r=\sqrt[3]{11/\pi}\approx1{,}52$ inci, $h=2r\approx3{,}04$ inci, $S\approx43{,}46\ \text{inci}^2$. (e) Grafik di bawah.

@@ P31 | Latihan 31 | Botol diremas | volume | 226
Luas permukaan botol silinder tidak berubah saat diremas. Apakah volumenya pasti tetap?
===
**Tidak.** Luas permukaan yang sama dapat melingkupi volume berbeda; bentuk berubah sehingga volume umumnya mengecil.

@@ P32 | Latihan 32 | Adakah luas minimum | geometri | 226
Persegi panjang berkeliling 20 ft memiliki luas maksimum $25\ \text{ft}^2$. Adakah dimensi dengan luas minimum?
===
**Tidak.** Luas $x(10-x)$ dengan $0<x<10$ dapat dibuat sedekat apa pun dengan nol, tetapi nol tidak tercapai oleh persegi panjang sejati.

@@ P33 | Latihan 33 | Kapsul dengan luas minimum | volume | 226
Benda berupa silinder dengan setengah bola di kedua ujung bervolume $14\ \text{cm}^3$. Jari-jari silinder berapa yang meminimumkan luas permukaan?
===
Dengan tinggi silinder $h\ge0$: $S=\dfrac{28}{r}+\dfrac{4\pi r^2}{3}$, $0<r\le\sqrt[3]{21/(2\pi)}$.

$S'=0$ tepat di batas $r=\sqrt[3]{21/(2\pi)}\approx1{,}50$ cm.

**Jawab:** $r\approx1{,}50$ cm dengan $h=0$: bentuk optimum adalah **bola**.

@@ P34 | Latihan 34 | Tangki industri berbiaya minimum | biaya | 226
Tangki berbentuk seperti latihan 33 bervolume $4.000\ \text{ft}^3$; ujung setengah bola dua kali lebih mahal per satuan luas daripada selimut. Dimensi termurah?
===
$C\propto 2\pi rh+8\pi r^2=\dfrac{8.000}{r}+\dfrac{16\pi r^2}{3}$. $C'=0\Rightarrow r^3=\dfrac{750}{\pi}$.

**Jawab:** $r\approx6{,}20$ ft, $h=4r\approx24{,}8$ ft.

@@ P35 | Latihan 35 | Segitiga sama sisi dan persegi | geometri | 226
Jumlah keliling segitiga sama sisi dan persegi 10. Dimensi untuk total luas minimum?
===
$3a+4b=10$, $A=\dfrac{\sqrt3}{4}a^2+b^2$, $A'=0\Rightarrow a=\dfrac{30}{9+4\sqrt3}\approx1{,}88$, $b=\dfrac{10-3a}{4}\approx1{,}09$.

@@ P36 | Latihan 36 | Kawat 20 ft menjadi dua bangun | geometri | 226
Seluruh kawat boleh dipakai untuk satu bangun. Bagaimana membaginya agar total luas maksimum untuk (a) segitiga sama sisi dan persegi, (b) persegi dan segilima, (c) segilima dan segienam, (d) segienam dan lingkaran?
===
Total luas cembung terhadap pembagian, sehingga maksimum di ujung: seluruh kawat untuk bangun dengan sisi lebih banyak.

| Kasus | (a) | (b) | (c) | (d) |
| Dipakai untuk | persegi | segilima | segienam | lingkaran |
| Luas (ft²) | 25 | 27,53 | 28,87 | 31,83 |

Pola: untuk keliling sama, makin banyak sisi makin besar luasnya. Jika kedua bangun harus ada, maksimum tidak tercapai.

@@ P37 | Latihan 37 | Balok terkuat dari gelondongan 20 inci | struktur | 226
$S=kh^2w$. Dimensi balok terkuat dari gelondongan berdiameter 20 inci?

{{fig:lo_p37}}
===
$S=kw(400-w^2)$, $S'=0\Rightarrow w=\dfrac{20}{\sqrt3}\approx11{,}55$ inci, $h=20\sqrt{\tfrac23}\approx16{,}33$ inci.

@@ P38 | Latihan 38 | Jaringan listrik ke dua pabrik | struktur | 226
Dua pabrik di $(\pm x,0)$, sumber di $(0,h)$, percabangan di $(0,y)$. Tentukan $y$ agar total panjang kabel minimum.

{{fig:lo_p38}}
===
$L=2\sqrt{x^2+y^2}+(h-y)$, $0\le y\le h$. $L'=\dfrac{2y}{\sqrt{x^2+y^2}}-1=0\Rightarrow y=\dfrac{x}{\sqrt3}$.

**Jawab:** $y=x/\sqrt3$ bila $h\ge x/\sqrt3$; jika tidak, $y=h$.

@@ P39 | Latihan 39 | Keliling segitiga terbesar | geometri | 226
Segitiga sama kaki dalam lingkaran berjari-jari 2. Tentukan keliling terbesar.

{{fig:lo_p39}}
===
$P=8\cos\dfrac\theta2+4\sin\theta$, $P'=4\left(\cos\theta-\sin\dfrac\theta2\right)=0\Rightarrow\theta=60^\circ$.

**Jawab:** $6\sqrt3\approx10{,}39$.

@@ P40 | Latihan 40 | Segitiga singgung terkecil | geometri | 226
Garis singgung $y=16-x^2$ di $(2; 12)$: tentukan luas segitiga di kuadran I, lalu titik singgung yang memberi luas terkecil.

{{fig:lo_p40}}
===
$y=-4x+20$: luas $\tfrac12(5)(20)=50$.

Di $x=a$: $A=\dfrac{(a^2+16)^2}{4a}$, $A'=0\Rightarrow a=\dfrac{4}{\sqrt3}$.

**Jawab:** titik $\left(\dfrac{4}{\sqrt3},\ \dfrac{32}{3}\right)$ dengan $A=\dfrac{256\sqrt3}{9}\approx49{,}3$.

@@ P41 | Latihan 41 | Pipa dari anjungan minyak | biaya | 226
Sumur 2 km lepas pantai, kilang 4 km sepanjang pantai. Pipa laut dua kali lebih mahal daripada pipa darat. Lintasan termurah?

{{fig:lo_p41}}
===
$C=2\sqrt{x^2+4}+(4-x)$, $C'=0\Rightarrow\dfrac{x}{\sqrt{x^2+4}}=\dfrac12\Rightarrow x=\dfrac{2}{\sqrt3}$.

**Jawab:** pipa laut ke titik $\approx1{,}15$ km dari titik pantai terdekat, lalu lewat darat.

@@ P42 | Latihan 42 | Tinggi lampu meja bundar | struktur | 226
$I=\dfrac{k\sin\alpha}{s^2}$ di tepi meja berdiameter 4 ft. Tinggi lampu optimum?

{{fig:lo_p42}}
===
$I=\dfrac{kh}{(h^2+4)^{3/2}}$, $I'\propto4-2h^2=0$.

**Jawab:** $h=\sqrt2\approx1{,}41$ ft.

@@ P43 | Latihan 43 | Pemandu wisata: dayung dan jalan | lintasan | 226
Perahu 2 mil dari pantai; tujuan $Q$ 3 mil sepanjang pantai dan 1 mil ke darat. Mendayung 2 mil/jam, berjalan 4 mil/jam. Ke titik pantai mana harus mendayung?

{{fig:lo_p43}}
===
$$T=\frac{\sqrt{x^2+4}}{2}+\frac{\sqrt{(3-x)^2+1}}{4}.$$

$T'=0$ dipenuhi $x=1$ (kedua ruas $T'$ bernilai $\tfrac{1}{2\sqrt5}$).

**Jawab:** 1 mil dari titik terdekat.

@@ P44 | Latihan 44 | Syarat waktu minimum | lintasan | 227
Pada latihan 43 dengan laju $v_1$ dan $v_2$, tunjukkan waktu minimum saat $\dfrac{\sin\theta_1}{v_1}=\dfrac{\sin\theta_2}{v_2}$.
===
$$T=\frac{\sqrt{x^2+d_1^2}}{v_1}+\frac{\sqrt{(a-x)^2+d_2^2}}{v_2}.$$

$T'=\dfrac{\sin\theta_1}{v_1}-\dfrac{\sin\theta_2}{v_2}=0$, dan $T''>0$. $\blacksquare$

@@ P45 | Latihan 45 | Jarak titik asal ke kurva | lintasan | 227
$f(x)=2-2\sin x$ pada $[0; \pi/2]$. (a) Jarak ke titik potong sumbu. (b) Fungsi jarak $d$. (c) Minimumnya.
===
(a) Ke $(0; 2)$: $2$. Ke $(\pi/2; 0)$: $\pi/2\approx1{,}57$.

(b) $d=\sqrt{x^2+(2-2\sin x)^2}$.

(c) Turunan nol saat $x=4\cos x\thinspace (1-\sin x)$, numerik $x\approx0{,}797$, $d_{\min}\approx0{,}980$.

@@ P46 | Latihan 46 | Hukum Snell | lintasan | 227
Tunjukkan pembiasan menurut Snell setara dengan latihan 44.

{{fig:lo_p46}}
===
Cahaya dari $P$ ke $Q$ memiliki fungsi waktu yang sama dengan latihan 44, dengan $v_1,v_2$ laju cahaya di tiap medium. Syarat minimumnya adalah $\dfrac{\sin\theta_1}{v_1}=\dfrac{\sin\theta_2}{v_2}$, yaitu Hukum Snell. Jadi cahaya menempuh lintasan berwaktu minimum. $\blacksquare$

@@ P47 | Latihan 47 | Kerucut dari lingkaran | volume | 227
Juring bersudut $\theta$ dibuang dari lingkaran berjari-jari 12 inci (lihat gambar), sisanya dibentuk menjadi kerucut. Tentukan $\theta$ untuk volume maksimum.

{{fig:lo_p47}}
===
Volume maksimum saat $r^2=\tfrac23(12^2)$, dan $2\pi r=12(2\pi-\theta)$.

**Jawab:** $\theta=2\pi\left(1-\sqrt{2/3}\right)\approx1{,}15$ rad $(\approx66^\circ)$.

@@ P48 | Latihan 48 | Saluran irigasi trapesium | air | 227
Penampang saluran trapesium sama kaki dengan tiga sisi 8 ft. Tentukan sudut $\theta$ untuk luas maksimum.

{{fig:lo_p48}}
===
(a)–(b)

| $\theta$ | 10° | 20° | 30° | 40° | 50° | 60° | 70° |
| $A$ | 22,1 | 42,5 | 59,7 | 72,7 | 80,5 | 83,1 | 80,7 |

(c) $A=64\sin\theta\thinspace (1+\cos\theta)$. (d) $A'=64(\cos\theta+\cos2\theta)=0\Rightarrow\theta=60^\circ$, $A=48\sqrt3\approx83{,}1\ \text{ft}^2$. (e) Grafik di bawah.

@@ P51 | Latihan 51 | Jalur induk: jumlah kuadrat | biaya | 228
Pusat distribusi di titik asal melayani titik $(4; 1)$, $(5; 6)$, $(10; 3)$ (mil) lewat jalur induk $y=mx$. Minimumkan $S_1=(4m-1)^2+(5m-6)^2+(10m-3)^2$.

{{fig:lo_p51}}
===
$S_1'=2(141m-64)=0\Rightarrow m=\dfrac{64}{141}\approx0{,}454$.

**Jawab:** $y=\dfrac{64}{141}x$; jumlah panjang cabang tegak $\approx6{,}09$ mil.

@@ P52 | Latihan 52 | Jalur induk: jumlah nilai mutlak | biaya | 228
Minimumkan $S_2=|4m-1|+|5m-6|+|10m-3|$.
===
$S_2$ linear sepotong-sepotong; cukup periksa titik patah $m=0{,}25; 0{,}3; 1{,}2$: nilainya $5{,}25$; $4{,}7$; $12{,}8$.

**Jawab:** $y=0{,}3x$ dengan jumlah $4{,}7$ mil.

@@ P53 | Latihan 53 | Jalur induk: jarak tegak lurus | biaya | 228
Minimumkan $S_3=\dfrac{|4m-1|+|5m-6|+|10m-3|}{\sqrt{m^2+1}}$.
===
Pada $[0{,}25; 0{,}3]$ fungsi turun, pada $[0{,}3; 1{,}2]$ naik (turunan sebanding $9-2m>0$); di luar interval itu nilainya lebih besar.

**Jawab:** $m=0{,}3$, $y=0{,}3x$, $S_3\approx4{,}50$ mil.

@@ P54 | Latihan 54 | Penampang silang dalam lingkaran | struktur | 228
Bentuk silang simetris berada dalam lingkaran berjari-jari $r$. Tulis luasnya sebagai fungsi $x$ dan sebagai fungsi $\theta$, lalu maksimumkan.

{{fig:lo_p54}}
===
Setengah panjang lengan $x$, setengah lebar $\sqrt{r^2-x^2}$:

(a) $A=8x\sqrt{r^2-x^2}-4(r^2-x^2)$, $\dfrac{r}{\sqrt2}\le x\le r$.

(b) Dengan $x=r\cos\theta$: $A=4r^2(\sin2\theta-\sin^2\theta)$, $A'=0\Rightarrow\tan2\theta=2$, $\theta\approx31{,}7^\circ$.

(c) Keduanya memberi $x=r\cos\theta\approx0{,}851r$ dan $A_{\max}=2(\sqrt5-1)r^2\approx2{,}47r^2$.

@@ P55 | Latihan 55 | Parabola mendatar | lintasan | 228
Titik pada $16x=y^2$ terdekat ke $(6; 0)$.
===
$d^2=(x-6)^2+16x=x^2+4x+36$ naik untuk $x\ge0$.

**Jawab:** titik $(0; 0)$, jarak $6$.

@@ P56 | Latihan 56 | Perhatikan domain | lintasan | 228
Titik pada $x=\sqrt{10y}$ terdekat ke $(0; 4)$.
===
$y=x^2/10$ dengan $x\ge0$. Turunan $d^2$ adalah $\dfrac{2x}{5}+\dfrac{x^3}{25}>0$ untuk $x>0$.

**Jawab:** titik $(0; 0)$, jarak $4$.

@@ P57 | Latihan 57 | Soal Putnam: maksimum berkendala | dasar | 228
Tentukan maksimum $f(x)=x^3-3x$ untuk $x$ yang memenuhi $x^4+36\le13x^2$.
===
Kendala $(x^2-4)(x^2-9)\le0$, yaitu $x\in[-3; -2]\cup[2; 3]$. $f'=3x^2-3>0$ di sana.

**Jawab:** $f(3)=18$.

@@ P58 | Latihan 58 | Soal Putnam: minimum aljabar | dasar | 228
Untuk $x>0$, tentukan minimum $\dfrac{(x+1/x)^6-(x^6+1/x^6)-2}{(x+1/x)^3+(x^3+1/x^3)}$.
===
Misalkan $a=(x+1/x)^3$, $b=x^3+1/x^3$. Pembilang $a^2-b^2$, sehingga pecahan $=a-b=3(x+1/x)$.

**Jawab:** minimum $6$ di $x=1$.

@@ L1 | Proyek Subbab | Waktu minimum mengitari dan menyeberangi danau | lintasan | 228
Dari $A$ di tepi danau berjari-jari 2 km, seseorang berjalan menyusuri tepi ke $B$ lalu berenang ke $C$ (seberang $A$). Laju jalan $v_1$, renang $v_2$, $0\le\theta\le\pi$. (a)–(d) Susun $f(\theta)$ dan turunannya. (e) $v_1=5$, $v_2=2$. (f) $v_1=3$, $v_2=2$.

{{fig:lo_l1}}
===
(a) Jalan: $2\theta$. (b) Renang: $4\cos(\theta/2)$.

(c)–(d) $f=\dfrac{2\theta}{v_1}+\dfrac{4\cos(\theta/2)}{v_2}$, $f'=\dfrac{2}{v_1}-\dfrac{2}{v_2}\sin\dfrac\theta2$.

(e) Titik kritis $\theta=2\arcsin0{,}4\approx0{,}823$ adalah **maksimum**. $f(0)=2$ jam, $f(\pi)\approx1{,}26$ jam: berjalan seluruhnya ($B=C$).

(f) Titik kritis $\theta=2\arcsin\tfrac23\approx1{,}459$ juga maksimum. $f(0)=2$, $f(\pi)\approx2{,}09$ jam: berenang langsung ($B=A$).
