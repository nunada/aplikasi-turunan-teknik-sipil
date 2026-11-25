@@ C1 | Contoh 1 | Kotak tanpa tutup dari lembaran seng | volume | 277
Dari selembar seng persegi 12 cm × 12 cm dipotong persegi kecil yang sama pada keempat sudutnya, lalu sisinya dilipat ke atas menjadi kotak tanpa tutup. Berapa panjang sisi persegi yang harus dipotong agar volume kotak maksimum?

{{fig:h_c1a h_c1b}}
===
Misalkan sisi potongan $x$. Alas kotak $(12-2x)\times(12-2x)$ dan tingginya $x$:

$$V(x)=x(12-2x)^2=4x^3-48x^2+144x,\qquad 0\le x\le 6.$$

$$V'(x)=12x^2-96x+144=12(x-2)(x-6).$$

Titik kritis di dalam domain hanya $x=2$. Bandingkan dengan ujung interval: $V(0)=0$, $V(2)=128$, $V(6)=0$.

{{fig:h_c1c}}

**Jawab:** potong persegi bersisi $2$ cm; volume maksimum $128\ \text{cm}^3$.

@@ C2 | Contoh 2 | Kaleng silinder 1 liter dengan bahan minimum | volume | 278
Rancang kaleng silinder tegak (tertutup) bervolume 1 liter. Dimensi berapa yang memakai bahan paling sedikit?

{{fig:h_c2}}
===
Dengan $r,h$ dalam cm: kendala $\pi r^2h=1.000$, tujuan $A=2\pi r^2+2\pi rh$. Substitusi $h=1.000/(\pi r^2)$:

$$A(r)=2\pi r^2+\frac{2.000}{r},\qquad r>0.$$

$$A'(r)=4\pi r-\frac{2.000}{r^2}=0\;\Rightarrow\; r=\sqrt[3]{\frac{500}{\pi}}\approx 5{,}42\text{ cm}.$$

Karena $A''(r)=4\pi+4.000/r^3>0$ untuk semua $r>0$, titik ini minimum mutlak. Tingginya $h=1.000/(\pi r^2)=2r\approx 10{,}84$ cm.

{{fig:h_c2g}}

**Jawab:** $r\approx5{,}42$ cm, $h\approx10{,}84$ cm (tinggi = diameter).

@@ C3 | Contoh 3 | Persegi panjang di dalam setengah lingkaran | geometri | 279
Sebuah persegi panjang dilukis di dalam setengah lingkaran berjari-jari 2. Tentukan luas terbesar dan dimensinya.

{{fig:h_c3}}
===
Sudut kanan atas $(x,\sqrt{4-x^2})$, sehingga

$$A(x)=2x\sqrt{4-x^2},\qquad 0\le x\le 2.$$

$$A'(x)=2\sqrt{4-x^2}-\frac{2x^2}{\sqrt{4-x^2}}=\frac{8-4x^2}{\sqrt{4-x^2}}=0\;\Rightarrow\;x=\sqrt2.$$

$A(0)=0$, $A(\sqrt2)=4$, $A(2)=0$.

**Jawab:** luas maksimum $4$, panjang $2\sqrt2$ dan tinggi $\sqrt2$.

@@ C4 | Contoh 4 | Prinsip Fermat dan Hukum Snell | lintasan | 279–280
Cahaya merambat dari titik $A$ (medium 1, laju $c_1$) ke titik $B$ (medium 2, laju $c_2$) melalui lintasan dengan waktu tersingkat. Tentukan syarat lintasannya.

{{fig:h_c4}}
===
Ambil $A=(0,a)$, $B=(d,-b)$ dan titik tembus $P=(x,0)$. Waktu tempuh:

$$t(x)=\frac{\sqrt{a^2+x^2}}{c_1}+\frac{\sqrt{b^2+(d-x)^2}}{c_2},\qquad 0\le x\le d.$$

$$t'(x)=\frac{x}{c_1\sqrt{a^2+x^2}}-\frac{d-x}{c_2\sqrt{b^2+(d-x)^2}}=\frac{\sin\theta_1}{c_1}-\frac{\sin\theta_2}{c_2}.$$

$t'(0)<0$ dan $t'(d)>0$, serta $t'$ naik (lihat latihan 70), sehingga ada tepat satu titik nol dan itu minimum.

**Jawab (Hukum Snell):** $\displaystyle\frac{\sin\theta_1}{c_1}=\frac{\sin\theta_2}{c_2}$.

Prinsip yang sama dipakai pada seismik refraksi untuk penyelidikan lapisan tanah.

@@ C6 | Contoh 6 | Jadwal pengiriman material kayu | biaya | 281–282
Seorang pengrajin membuat 5 meja per hari. Sekali kirim material berbiaya 5.000 dolar, sedangkan penyimpanan 10 dolar per unit per hari (1 unit = material untuk 1 meja). Berapa unit dipesan tiap kali dan setiap berapa hari agar biaya rata-rata harian minimum?

{{fig:h_c6}}
===
Jika dikirim tiap $x$ hari, pesanan $5x$ unit dan stok rata-rata $5x/2$. Biaya per siklus $=5.000+\frac{5x}{2}\cdot x\cdot 10$. Biaya rata-rata harian:

$$c(x)=\frac{5.000}{x}+25x,\qquad x>0.$$

$$c'(x)=-\frac{5.000}{x^2}+25=0\;\Rightarrow\;x=\sqrt{200}\approx14{,}14,\qquad c''(x)=\frac{10.000}{x^3}>0.$$

$c(\sqrt{200})=500\sqrt2\approx 707{,}11$ dolar/hari.

**Jawab:** pesan sekitar $5\times14=70$ unit setiap 14 hari.

@@ P1 | Latihan 1 | Keliling minimum | geometri | 282
Berapa keliling terkecil persegi panjang berluas $16\text{ cm}^2$, dan berapa dimensinya?
===
Sisi $x$ dan $16/x$: $P(x)=2x+\dfrac{32}{x}$, $x>0$. $P'(x)=2-\dfrac{32}{x^2}=0\Rightarrow x=4$, dan $P''>0$.

**Jawab:** persegi $4\times4$ cm, keliling minimum $16$ cm.

@@ P2 | Latihan 2 | Luas maksimum adalah persegi | geometri | 282
Tunjukkan bahwa di antara semua persegi panjang berkeliling 8 m, yang luasnya terbesar adalah persegi.
===
Sisi $x$ dan $4-x$: $A=x(4-x)$, $0\le x\le4$. $A'=4-2x=0\Rightarrow x=2$. $A(0)=A(4)=0<A(2)=4$.

Jadi maksimum terjadi saat kedua sisi $2$ m, yaitu persegi. $\blacksquare$

@@ P3 | Latihan 3 | Persegi panjang dalam segitiga siku-siku sama kaki | geometri | 282
Persegi panjang dilukis di dalam segitiga siku-siku sama kaki dengan sisi miring 2 satuan.
(a) Nyatakan ordinat $P$ dalam $x$. (b) Nyatakan luasnya dalam $x$. (c) Tentukan luas terbesar dan dimensinya.

{{fig:h_p3}}
===
(a) Garis $AB$ melalui $(1;\,0)$ dan $(0;\,1)$: $y=1-x$.

(b) $A(x)=2x(1-x)$, $0\le x\le1$.

(c) $A'=2-4x=0\Rightarrow x=\tfrac12$.

**Jawab:** luas maksimum $\tfrac12$, dengan panjang $1$ dan tinggi $\tfrac12$.

@@ P4 | Latihan 4 | Persegi panjang di bawah parabola | geometri | 282
Alas persegi panjang berada pada sumbu-$x$ dan dua sudut atasnya pada $y=12-x^2$. Tentukan luas terbesar dan dimensinya.

{{fig:h_p4}}
===
$A(x)=2x(12-x^2)=24x-2x^3$, $0\le x\le\sqrt{12}$. $A'=24-6x^2=0\Rightarrow x=2$.

**Jawab:** lebar $4$, tinggi $8$, luas maksimum $32$.

@@ P5 | Latihan 5 | Kotak dari karton 24 cm × 45 cm | volume | 282
Kotak tanpa tutup dibuat dari karton $24\times45$ cm dengan memotong persegi di keempat sudut lalu melipat sisinya. Tentukan dimensi dan volume terbesar.

{{fig:h_p5}}
===
$V(x)=x(24-2x)(45-2x)$, $0\le x\le12$.

$$V'(x)=12x^2-276x+1.080=12(x-5)(x-18).$$

Hanya $x=5$ di dalam domain; $V(0)=V(12)=0$.

**Jawab:** $35\times14\times5$ cm, volume $2.450\ \text{cm}^3$.

@@ P6 | Latihan 6 | Segitiga pada sudut kuadran pertama | geometri | 282
Ruas garis sepanjang 20 satuan dari $(a,0)$ ke $(0,b)$ memotong sudut kuadran pertama. Tunjukkan bahwa luas segitiga terbesar saat $a=b$.

{{fig:h_p6}}
===
$a^2+b^2=400$, $A=\tfrac12 a\sqrt{400-a^2}$. Maksimumkan $f(a)=A^2=\tfrac14(400a^2-a^4)$:

$$f'(a)=\tfrac14(800a-4a^3)=0\;\Rightarrow\;a^2=200.$$

Maka $b^2=400-200=200$, sehingga $a=b=10\sqrt2$ (luas $100$). $\blacksquare$

@@ P7 | Latihan 7 | Pagar tiga sisi di tepi sungai | struktur | 282
Lahan persegi panjang dibatasi sungai di satu sisi dan pagar listrik tunggal di tiga sisi lainnya. Dengan 800 m kawat, berapa luas terbesar dan dimensinya?

{{fig:h_p7}}
===
$A(x)=x(800-2x)$, $0\le x\le400$. $A'=800-4x=0\Rightarrow x=200$.

**Jawab:** $200$ m (tegak lurus sungai) $\times\,400$ m; luas $80.000\ \text{m}^2$.

@@ P8 | Latihan 8 | Pagar terpendek untuk lahan terbagi dua | struktur | 282
Lahan persegi panjang $216\ \text{m}^2$ dipagari dan dibagi dua sama besar dengan pagar sejajar salah satu sisi. Tentukan dimensi luar dengan total pagar terpendek.

{{fig:h_p8}}
===
Dimensi $x\times y$ dengan pagar pembagi sejajar $y$: $F=2x+3y$, $xy=216$.

$$F(x)=2x+\frac{648}{x},\quad F'=2-\frac{648}{x^2}=0\Rightarrow x=18,\;y=12.$$

**Jawab:** $18\times12$ m dengan total pagar $72$ m.

@@ P9 | Latihan 9 | Tangki baja paling ringan | volume | 283
Rancang tangki baja $4\ \text{m}^3$ beralas persegi, tanpa tutup, dari pelat tipis yang dilas. (a) Dimensi agar tangki seringan mungkin? (b) Bagaimana berat diperhitungkan?
===
(a) Alas $x$, tinggi $h=4/x^2$. Luas pelat:

$$S(x)=x^2+4xh=x^2+\frac{16}{x},\quad S'=2x-\frac{16}{x^2}=0\Rightarrow x=2,\;h=1.$$

**Jawab:** alas $2\times2$ m, tinggi $1$ m ($S=12\ \text{m}^2$).

(b) Untuk tebal pelat seragam, berat sebanding dengan luas permukaan, jadi meminimumkan $S$ sama dengan meminimumkan berat.

@@ P10 | Latihan 10 | Tangki penampung air hujan | biaya | 283
Tangki terbuka $20\ \text{m}^3$ beralas persegi sisi $x$ m dan kedalaman $y$ m ditanam rata tanah. (a) Jika biaya $c=5(x^2+4xy)+10xy$, tentukan $x,y$ yang meminimumkannya. (b) Berikan skenario untuk fungsi biaya tersebut.

{{fig:h_p10}}
===
(a) $y=20/x^2$, sehingga $c(x)=5x^2+30xy=5x^2+\dfrac{600}{x}$.

$$c'=10x-\frac{600}{x^2}=0\Rightarrow x=\sqrt[3]{60}\approx3{,}91\text{ m},\qquad y=\frac{20}{x^2}=\frac{x}{3}\approx1{,}31\text{ m}.$$

(b) $5(x^2+4xy)$: biaya material dasar dan empat dinding (5 per m²). $10xy$: biaya galian yang sebanding dengan hasil kali $xy$.

@@ P11 | Latihan 11 | Poster dengan margin | geometri | 283
Poster memuat area cetak $312{,}5\ \text{cm}^2$, margin 10 cm atas dan bawah serta 5 cm kiri dan kanan. Dimensi total berapa yang meminimumkan kertas?

{{fig:h_p11}}
===
Area cetak lebar $x$, tinggi $312{,}5/x$:

$$A(x)=(x+10)\left(\frac{312{,}5}{x}+20\right)=512{,}5+20x+\frac{3.125}{x}.$$

$A'=20-\dfrac{3.125}{x^2}=0\Rightarrow x=12{,}5$, tinggi cetak $25$.

**Jawab:** poster $22{,}5\times45$ cm.

@@ P12 | Latihan 12 | Kerucut terbesar di dalam bola | volume | 283
Tentukan volume kerucut tegak terbesar yang dapat dimasukkan ke dalam bola berjari-jari 3.

{{fig:h_p12}}
===
Dengan $y$ = jarak pusat bola ke alas dan $x$ = jari-jari alas: $x^2=9-y^2$, tinggi $3+y$.

$$V(y)=\frac{\pi}{3}(9-y^2)(3+y),\quad V'(y)=-\pi(y+3)(y-1)=0\Rightarrow y=1.$$

**Jawab:** $V_{\max}=\dfrac{32\pi}{3}$ satuan volume.

@@ P13 | Latihan 13 | Sudut apit untuk luas segitiga maksimum | geometri | 283
Dua sisi segitiga panjangnya $a$ dan $b$ dengan sudut apit $\theta$. Nilai $\theta$ berapa yang memaksimumkan luas?

{{fig:h_p13}}
===
$A=\tfrac12ab\sin\theta$, $0<\theta<\pi$. $A'=\tfrac12ab\cos\theta=0\Rightarrow\theta=\pi/2$; tanda $A'$ berubah dari positif ke negatif.

**Jawab:** $\theta=90^\circ$.

@@ P14 | Latihan 14 | Kaleng tanpa tutup paling ringan | volume | 283
Tentukan dimensi kaleng silinder tanpa tutup paling ringan bervolume $1.000\ \text{cm}^3$. Bandingkan dengan Contoh 2.
===
$S=\pi r^2+2\pi rh$ dengan $h=1.000/(\pi r^2)$: $S(r)=\pi r^2+\dfrac{2.000}{r}$.

$$S'=2\pi r-\frac{2.000}{r^2}=0\Rightarrow r=\frac{10}{\sqrt[3]{\pi}}\approx6{,}83\text{ cm},\qquad h=r.$$

**Jawab:** $r=h\approx6{,}83$ cm. Pada kaleng tertutup $h=2r$; tanpa tutup, kaleng optimal lebih pendek dan lebar.

@@ P15 | Latihan 15 | Kaleng dengan sisa potongan bahan | volume | 283
Kaleng silinder $1.000\ \text{cm}^3$: selimut dipotong tanpa sisa, tetapi tutup dan alas dipotong dari persegi sisi $2r$, sehingga bahan terpakai $A=8r^2+2\pi rh$. Berapa rasio $h:r$ paling hemat?

{{fig:h_p15}}
===
$A(r)=8r^2+\dfrac{2.000}{r}$, $A'=16r-\dfrac{2.000}{r^2}=0\Rightarrow r^3=125$, $r=5$ cm.

$h=\dfrac{1.000}{25\pi}=\dfrac{40}{\pi}$.

**Jawab:** $\dfrac{h}{r}=\dfrac{8}{\pi}\approx2{,}55$.

@@ P16 | Latihan 16 | Kotak bertutup dari karton 30 cm × 45 cm | volume | 283
Dari karton $30\times45$ cm dibuang dua persegi sisi $x$ pada sudut salah satu sisi 30 cm dan dua persegi panjang di sudut lain sehingga terbentuk kotak bertutup. (a) Tulis $V(x)$. (b) Tentukan domain dan gambarkan grafiknya. (c) Maksimum secara grafis. (d) Konfirmasi analitis.

{{fig:h_p16}}
===
(a) Panjang 45 cm terbagi menjadi $x+b+x+b$, jadi $b=\dfrac{45-2x}{2}$. Alas $b\times(30-2x)$, tinggi $x$:

$$V(x)=x(30-2x)\frac{45-2x}{2}=2x^3-75x^2+675x.$$

(b) Domain $0<x<15$.

{{fig:h_p16g}}

(c) Dari grafik, puncak di sekitar $x\approx5{,}9$ dengan $V\approx1.780$.

(d) $V'=6x^2-150x+675=0\Rightarrow x=\dfrac{25-5\sqrt7}{2}\approx5{,}89$ cm (akar lain di luar domain).

**Jawab:** $V_{\max}\approx1.782{,}5\ \text{cm}^3$.

@@ P17 | Latihan 17 | Merancang koper dari karton | volume | 283
Karton $60\times90$ cm dilipat dua menjadi $60\times45$ cm; empat persegi sisi $x$ dipotong di sudut lipatan, karton dibuka, lalu enam sayap dilipat menjadi koper. (a) $V(x)$. (b) Tentukan domain dan gambarkan grafiknya. (c)–(d) Volume maksimum. (e) Nilai $x$ untuk $V=17.500\ \text{cm}^3$. (f) Bahas isu pada (b).

{{fig:h_p17}}
===
(a) $V(x)=2x(60-2x)(45-2x)=8x^3-420x^2+5.400x$.

(b) Semua ukuran positif: $0<x<22{,}5$.

{{fig:h_p17g}}

(c)–(d) $V'=24(x^2-35x+225)=0\Rightarrow x=\dfrac{35-5\sqrt{13}}{2}\approx8{,}49$ cm, $V_{\max}\approx20.468\ \text{cm}^3$.

(e) $8x^3-420x^2+5.400x-17.500=0$ terfaktor menjadi $4(x-5)(2x^2-95x+875)=0$. Akar dalam domain: $x=5$ cm atau $x=12{,}5$ cm.

(f) Domain ditentukan sisi terpendek bidang terlipat ($45-2x>0$). Di ujung domain kotak merosot (volume nol), dan satu nilai volume dapat dicapai oleh dua desain berbeda.

@@ P18 | Latihan 18 | Persegi panjang di bawah lengkung kosinus | geometri | 283
Persegi panjang dilukis di bawah lengkung $y=4\cos(0{,}5x)$, $-\pi\le x\le\pi$. Tentukan dimensi dan luas terbesar.

{{fig:h_p18}}
===
$A(x)=8x\cos(x/2)$, $0\le x\le\pi$.

$$A'=8\cos\frac x2-4x\sin\frac x2=0\iff u\tan u=1,\;u=\frac x2.$$

Secara numerik (Newton) $u\approx0{,}8603$, jadi $x\approx1{,}7207$.

**Jawab:** lebar $2x\approx3{,}44$, tinggi $\approx2{,}61$, luas $\approx8{,}98$.

@@ P19 | Latihan 19 | Silinder terbesar di dalam bola | volume | 284
Tentukan dimensi silinder tegak bervolume maksimum di dalam bola berjari-jari 10 cm, beserta volumenya.

{{fig:h_p19}}
===
$r^2+(h/2)^2=100$, sehingga $V(h)=\pi\left(100-\dfrac{h^2}{4}\right)h$, $0\le h\le20$.

$$V'=\pi\left(100-\frac{3h^2}{4}\right)=0\Rightarrow h=\frac{20}{\sqrt3}\approx11{,}55,\quad r=10\sqrt{\tfrac23}\approx8{,}16.$$

**Jawab:** $V_{\max}=\dfrac{4.000\pi}{3\sqrt3}\approx2.418\ \text{cm}^3$.

@@ P20 | Latihan 20 | Paket pos berujung persegi | volume | 284
(a) Panjang ditambah lingkar (girth) paket tidak boleh melebihi 276 cm. Dimensi berapa yang memberi volume terbesar untuk kotak berpenampang ujung persegi? (b) Gambarkan grafik volume terhadap panjang dan bandingkan.

{{fig:h_p20}}
===
(a) Penampang $x\times x$, panjang $L=276-4x$: $V=x^2(276-4x)$. $V'=552x-12x^2=0\Rightarrow x=46$.

**Jawab:** $46\times46\times92$ cm, $V=194.672\ \text{cm}^3$.

(b) Dalam $L$: $V(L)=L\left(\dfrac{276-L}{4}\right)^2$.

{{fig:h_p20g}}

Puncak grafik di $L=92$, sesuai bagian (a).

@@ P21 | Latihan 21 | Paket pos bersisi persegi | volume | 284
(Lanjutan latihan 20.) Kotak berdimensi $h\times h\times w$ dengan lingkar $2h+2w$ dan panjang $h$. (a) Tentukan dimensi kotak agar volumenya maksimum. (b) Gambarkan grafik $V(h)$.

{{fig:h_p21}}
===
(a) $h+(2h+2w)=276\Rightarrow w=138-1{,}5h$. $V=h^2(138-1{,}5h)$, $V'=276h-4{,}5h^2=0\Rightarrow h=\dfrac{184}{3}$.

**Jawab:** $h\approx61{,}33$ cm, $w=46$ cm, $V\approx173.041{,}78\ \text{cm}^3$.

(b)

{{fig:h_p21g}}

Puncaknya di $h\approx61{,}3$.

@@ P22 | Latihan 22 | Jendela dengan kaca bening dan kaca berwarna | struktur | 284
Jendela berbentuk persegi panjang ditambah setengah lingkaran di atasnya. Kaca setengah lingkaran meneruskan cahaya setengah dari kaca bening per satuan luas. Keliling total tetap. Tentukan proporsi yang meneruskan cahaya terbanyak.

{{fig:h_p22}}
===
Jari-jari $r$, tinggi persegi panjang $h$: $P=2r+2h+\pi r$. Cahaya sebanding dengan

$$L=2rh+\tfrac12\cdot\tfrac{\pi r^2}{2}=Pr-2r^2-\frac{3\pi}{4}r^2.$$

$$L'=P-\left(4+\frac{3\pi}{2}\right)r=0\Rightarrow r=\frac{2P}{8+3\pi},\qquad h=\frac{(4+\pi)P}{2(8+3\pi)}.$$

**Jawab:** $\dfrac{\text{lebar}}{\text{tinggi persegi panjang}}=\dfrac{2r}{h}=\dfrac{8}{4+\pi}\approx1{,}12$.

@@ P23 | Latihan 23 | Silo silinder beratap setengah bola | biaya | 284
Silo (tanpa lantai) berbentuk silinder beratap setengah bola. Biaya per satuan luas atap dua kali biaya dinding. Volume tetap. Tentukan dimensi berbiaya minimum.

{{fig:h_p23}}
===
$V=\pi r^2h+\tfrac23\pi r^3\Rightarrow h=\dfrac{V}{\pi r^2}-\dfrac{2r}{3}$. Dengan $c$ = biaya dinding per satuan luas:

$$C(r)=c\,(2\pi rh)+2c\,(2\pi r^2)=c\left(\frac{2V}{r}+\frac{8\pi r^2}{3}\right).$$

$$C'=0\Rightarrow r=\left(\frac{3V}{8\pi}\right)^{1/3},\qquad h=\frac{8r}{3}-\frac{2r}{3}=2r.$$

**Jawab:** $r=\sqrt[3]{3V/(8\pi)}$ dan tinggi silinder $h=2r$.

@@ P24 | Latihan 24 | Talang trapesium dengan sudut optimum | air | 284
Talang pada gambar memiliki alas 1 ft, dua dinding 1 ft, panjang 20 ft. Hanya sudut $\theta$ (terhadap vertikal) yang dapat diubah. $\theta$ berapa yang memaksimumkan volume?

{{fig:h_p24}}
===
Luas penampang $=\cos\theta\,(1+\sin\theta)$, $0\le\theta<\pi/2$, dan $V=20A$.

$$A'=-\sin\theta(1+\sin\theta)+\cos^2\theta=-(2\sin\theta-1)(\sin\theta+1)=0\Rightarrow\theta=\frac{\pi}{6}.$$

**Jawab:** $\theta=30^\circ$, $V_{\max}=15\sqrt3\approx25{,}98\ \text{ft}^3$.

@@ P25 | Latihan 25 | Lipatan kertas terpendek | geometri | 284
Salah satu sudut kertas $21{,}6\times28$ cm diletakkan pada tepi panjang di seberangnya lalu diratakan. (a) Tunjukkan $L^2=\dfrac{2x^3}{2x-21{,}6}$. (b) $x$ yang meminimumkan $L^2$? (c) Panjang lipatan minimum?

{{fig:h_p25}}
===
(a) Tempatkan $A=(0;\,0)$, $P=(x;\,0)$, $R=(0;\,y)$. $Q$ adalah bayangan $A$ terhadap garis $PR$, absisnya $\dfrac{2xy^2}{x^2+y^2}=21{,}6$. Diperoleh $y^2=\dfrac{21{,}6x^2}{2x-21{,}6}$, sehingga

$$L^2=x^2+y^2=\frac{2x^3}{2x-21{,}6}.$$

(b) Turunannya sebanding dengan $x^2(4x-64{,}8)$, nol di $x=16{,}2$ cm (domain $10{,}8<x\le21{,}6$).

(c) $L^2=787{,}32$, jadi $L_{\min}\approx28{,}06$ cm. Saat itu $y\approx22{,}9\le28$, sehingga lipatan muat di kertas.

@@ P26 | Latihan 26 | Dua cara membentuk silinder | volume | 284
Persegi panjang $x\times y$ berkeliling 36 cm. (a) Digulung menjadi selimut silinder (keliling $x$, tinggi $y$). (b) Diputar terhadap sisi $y$. Dalam tiap kasus, $x,y$ berapa yang memaksimumkan volume?

{{fig:h_p26}}
===
$y=18-x$.

(a) $V=\pi\left(\dfrac{x}{2\pi}\right)^2y=\dfrac{x^2(18-x)}{4\pi}$; $V'\propto36x-3x^2=0\Rightarrow x=12,\;y=6$.

(b) $V=\pi x^2(18-x)$; turunannya nol di titik yang sama: $x=12$, $y=6$.

**Jawab:** keduanya $x=12$ cm, $y=6$ cm.

@@ P27 | Latihan 27 | Kerucut dari segitiga yang diputar | volume | 285
Segitiga siku-siku bersisi miring $\sqrt3$ m diputar terhadap salah satu kakinya. Tentukan jari-jari, tinggi, dan volume kerucut terbesar.

{{fig:h_p27}}
===
$r^2=3-h^2$, $V=\dfrac{\pi}{3}(3h-h^3)$, $V'=\pi(1-h^2)=0\Rightarrow h=1$.

**Jawab:** $h=1$ m, $r=\sqrt2$ m, $V=\dfrac{2\pi}{3}\ \text{m}^3$.

@@ P28 | Latihan 28 | Titik pada garis yang terdekat ke titik asal | lintasan | 285
Tentukan titik pada garis $\dfrac xa+\dfrac yb=1$ yang paling dekat dengan titik asal.

{{fig:h_p28}}
===
Minimumkan $D=x^2+y^2$ dengan $y=b\left(1-\dfrac xa\right)$:

$$D'=2x-\frac{2b^2}{a}\left(1-\frac xa\right)=0\Rightarrow x=\frac{ab^2}{a^2+b^2}.$$

**Jawab:** $\left(\dfrac{ab^2}{a^2+b^2},\ \dfrac{a^2b}{a^2+b^2}\right)$.

@@ P29 | Latihan 29 | Bilangan ditambah kebalikannya | dasar | 285
Tentukan bilangan positif yang jumlahnya dengan kebalikannya sekecil mungkin.
===
$f(x)=x+\dfrac1x$, $f'=1-\dfrac1{x^2}=0\Rightarrow x=1$; $f''>0$.

**Jawab:** $x=1$ (jumlah $2$).

@@ P30 | Latihan 30 | Kebalikan ditambah empat kali kuadrat | dasar | 285
Tentukan bilangan positif sehingga jumlah kebalikannya dan empat kali kuadratnya minimum.
===
$f=\dfrac1x+4x^2$, $f'=-\dfrac1{x^2}+8x=0\Rightarrow x=\tfrac12$; $f''>0$.

**Jawab:** $x=\tfrac12$ (nilai $3$).

@@ P31 | Latihan 31 | Kawat menjadi segitiga dan lingkaran | geometri | 285
Kawat $b$ m dipotong dua: satu menjadi segitiga sama sisi, satu menjadi lingkaran. Agar jumlah luas minimum, berapa panjang tiap potongan?

{{fig:h_p31}}
===
Potongan segitiga $x$:

$$A(x)=\frac{\sqrt3}{36}x^2+\frac{(b-x)^2}{4\pi},\quad A'=\frac{\sqrt3x}{18}-\frac{b-x}{2\pi}=0.$$

**Jawab:** segitiga $x=\dfrac{9b}{9+\sqrt3\pi}$, lingkaran $\dfrac{\sqrt3\pi b}{9+\sqrt3\pi}$.

@@ P32 | Latihan 32 | Kawat menjadi persegi dan lingkaran | geometri | 285
Ulangi latihan 31 jika satu potongan dibentuk persegi.
===
$A(x)=\dfrac{x^2}{16}+\dfrac{(b-x)^2}{4\pi}$, $A'=\dfrac x8-\dfrac{b-x}{2\pi}=0$.

**Jawab:** persegi $\dfrac{4b}{4+\pi}$, lingkaran $\dfrac{\pi b}{4+\pi}$.

@@ P33 | Latihan 33 | Kawat penggantung berbentuk Y | struktur | 285
Beban $D$ digantung 5 m di bawah garis horizontal $AB$ dengan kawat berbentuk Y; $A$ dan $B$ berjarak 4 m. Berapa panjang total kawat minimum?

{{fig:h_p33}}
===
Misalkan $C$ berada $y$ m di bawah $AB$:

$$L(y)=2\sqrt{4+y^2}+(5-y),\quad L'=\frac{2y}{\sqrt{4+y^2}}-1=0\Rightarrow y=\frac{2}{\sqrt3}.$$

**Jawab:** $L_{\min}=5+2\sqrt3\approx8{,}46$ m.

@@ P34 | Latihan 34 | Biaya kawat dengan dua mutu | biaya | 285
Pada latihan 33, segmen vertikal $CD$ berharga 1 dolar/m, sedangkan $AC$ dan $CB$ 2 dolar/m. Berapa biaya minimum?
===
$$K(y)=4\sqrt{4+y^2}+(5-y),\quad K'=\frac{4y}{\sqrt{4+y^2}}-1=0\Rightarrow y=\frac{2}{\sqrt{15}}.$$

**Jawab:** $K_{\min}=5+2\sqrt{15}\approx12{,}75$ dolar.

@@ P35 | Latihan 35 | Persegi panjang dalam segitiga 3-4-5 | geometri | 285
Tentukan persegi panjang terluas yang dapat dilukis dalam segitiga siku-siku pada gambar.

{{fig:h_p35}}
===
Dari kesebangunan: $\dfrac w3+\dfrac h4=1$, jadi $A=4w\left(1-\dfrac w3\right)$, $A'=4-\dfrac{8w}{3}=0\Rightarrow w=1{,}5$.

**Jawab:** $w=1{,}5$, $h=2$, luas $3$.

@@ P36 | Latihan 36 | Persegi panjang dalam setengah lingkaran | geometri | 285
Tentukan persegi panjang terluas di dalam setengah lingkaran berjari-jari 3.

{{fig:h_p36}}
===
$w=2x$, $h=\sqrt{9-x^2}$, $A=2x\sqrt{9-x^2}$, $A'=\dfrac{2(9-2x^2)}{\sqrt{9-x^2}}=0\Rightarrow x=\dfrac{3}{\sqrt2}$.

**Jawab:** $w=3\sqrt2$, $h=\dfrac{3\sqrt2}{2}$, luas $9$.

@@ P37 | Latihan 37 | Parameter untuk minimum dan titik belok | dasar | 285
Nilai $a$ berapa membuat $f(x)=x^2+\dfrac ax$ memiliki (a) minimum lokal di $x=2$; (b) titik belok di $x=1$?
===
(a) $f'=2x-a/x^2$; $f'(2)=0\Rightarrow a=16$, dan $f''(2)=6>0$.

(b) $f''=2+2a/x^3$; $f''(1)=0\Rightarrow a=-1$ (tanda $f''$ berubah di $x=1$).

@@ P38 | Latihan 38 | Parameter polinomial derajat tiga | dasar | 285
Tentukan $a,b$ agar $f(x)=x^3+ax^2+bx$ memiliki (a) maksimum lokal di $x=-1$ dan minimum lokal di $x=3$; (b) minimum lokal di $x=4$ dan titik belok di $x=1$.
===
$f'=3x^2+2ax+b$.

(a) Akar $f'$ adalah $-1$ dan $3$: $f'=3(x+1)(x-3)$, sehingga $a=-3$, $b=-9$.

(b) $f''(1)=6+2a=0\Rightarrow a=-3$; $f'(4)=48-24+b=0\Rightarrow b=-24$.

@@ P39 | Latihan 39 | Kerucut maksimum dalam bola satuan | volume | 285
Kerucut tegak berada di dalam bola berjari-jari 1 (titik puncak dan lingkaran alas pada bola). Tentukan $h$ dan $r$ untuk volume maksimum.

{{fig:h_p39}}
===
$r^2=1-(h-1)^2=2h-h^2$. $V=\dfrac\pi3(2h^2-h^3)$, $V'=\dfrac\pi3h(4-3h)=0$.

**Jawab:** $h=\dfrac43$, $r=\dfrac{2\sqrt2}{3}$, $V=\dfrac{32\pi}{81}$.

@@ P40 | Latihan 40 | Persegi panjang di bawah kurva eksponensial | geometri | 285
Tentukan dimensi persegi panjang terluas pada gambar (di bawah $y=e^{-x}$).

{{fig:h_p40}}
===
$A=xe^{-x}$, $A'=(1-x)e^{-x}=0\Rightarrow x=1$.

**Jawab:** alas $1$, tinggi $1/e$, luas $1/e$.
