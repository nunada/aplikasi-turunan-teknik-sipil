@@ C1 | Contoh 1 | Mengisi tangki kerucut | air | 206–207
Air masuk ke tangki kerucut (puncak di bawah) dengan debit $0{,}25\ \text{m}^3$/menit. Tinggi tangki 3 m dan jari-jari alasnya 1,5 m. Seberapa cepat muka air naik saat kedalaman air 1,8 m?

{{fig:th_c1}}
===
Misalkan $x$ jari-jari muka air dan $y$ kedalaman. Dari kesebangunan $x=y/2$, sehingga

$$V=\frac{\pi}{3}x^2y=\frac{\pi}{12}y^3,\qquad\frac{dV}{dt}=\frac{\pi}{4}y^2\frac{dy}{dt}.$$

Dengan $y=1{,}8$ dan $dV/dt=0{,}25$:

**Jawab:** $\dfrac{dy}{dt}=\dfrac{1}{3{,}24\pi}\approx0{,}098$ m/menit.

@@ C2 | Contoh 2 | Balon udara dipantau dari alat ukur sudut | laju | 207–208
Balon udara naik tegak. Pengukur jarak berada 150 m dari titik lepas landas. Saat sudut elevasi $\pi/4$, sudut itu bertambah 0,14 rad/menit. Seberapa cepat balon naik?

{{fig:th_c2}}
===
$y=150\tan\theta$, sehingga $\dfrac{dy}{dt}=150\sec^2\theta\thinspace \dfrac{d\theta}{dt}$.

**Jawab:** $\dfrac{dy}{dt}=150(2)(0{,}14)=42$ m/menit.

Prinsip ini dipakai dalam pengukuran tinggi dengan theodolit.

@@ C3 | Contoh 3 | Mobil polisi mengejar | lintasan | 208
Mobil polisi mendekati persimpangan siku dari utara dengan laju 100 km/jam. Saat polisi 0,6 km di utara dan mobil buruan 0,8 km di timur persimpangan, jarak keduanya bertambah 30 km/jam. Berapa laju mobil buruan?

{{fig:th_c3}}
===
$s^2=x^2+y^2$ memberi $s\dot s=x\dot x+y\dot y$, dengan $s=1$ dan $\dot y=-100$:

$$30=0{,}8\thinspace \dot x+0{,}6(-100).$$

**Jawab:** $\dot x=112{,}5$ km/jam.

@@ C4 | Contoh 4 | Perpotongan garis singgung lingkaran | gerak | 209
Partikel $P$ bergerak searah jarum jam dengan laju tetap pada lingkaran berjari-jari 10 m, dari $(0; 10)$ ke $(10; 0)$ selama 30 s. Garis singgung di $P$ memotong sumbu-$x$ di $Q$. Seberapa cepat $Q$ bergerak saat berjarak 20 m dari pusat?

{{fig:th_c4}}
===
$x\cos\theta=10$ dengan $\dot\theta=-\pi$ rad/menit. Turunkan:

$$\dot x\cos\theta-x\sin\theta\thinspace \dot\theta=0.$$

Saat $x=20$: $\cos\theta=\tfrac12$, $\sin\theta=\tfrac{\sqrt3}{2}$.

**Jawab:** $\dot x=-20\sqrt3\thinspace \pi\approx-108{,}8$ m/menit, yaitu mendekati pusat sekitar 109 m/menit.

@@ C5 | Contoh 5 | Pesawat dipantau radar | gerak | 209–210
Pesawat terbang pada ketinggian tetap 10.000 m menuju sebuah pulau. Saat pertama terdeteksi, sudut elevasi dari radar $30^\circ$ dan radar berputar ke atas $\tfrac13$ derajat per detik. Berapa laju pesawat dalam km/jam?

{{fig:th_c5}}
===
Dalam kilometer $x=10\cot\theta$, sehingga $\dot x=-10\csc^2\theta\thinspace \dot\theta$, dengan $\csc^2 30^\circ=4$ dan

$$\dot\theta=\tfrac13\cdot\frac{\pi}{180}\cdot3.600\ \text{rad/jam}.$$

**Jawab:** $\dot x\approx-838$ km/jam: pesawat mendekat dengan laju 838 km/jam.

@@ C6 | Contoh 6 | Pekerja mengangkat beban dengan katrol | struktur | 210
Tali melewati katrol setinggi 7,5 m. Satu ujung memegang beban, ujung lain dipegang pekerja setinggi 1,5 m dari tanah. Panjang tali 13,5 m dan pekerja menjauh 1,2 m/s. Seberapa cepat beban terangkat saat tangan pekerja 6,3 m dari garis tegak katrol?

{{fig:th_c6}}
===
Dengan $O$ tepat di bawah katrol setinggi tangan, katrol 6 m di atas $O$:

$$6-h+z=13{,}5,\qquad 6^2+x^2=z^2\ \Rightarrow\ 36+x^2=(7{,}5+h)^2.$$

$$\dot h=\frac{x\thinspace \dot x}{7{,}5+h}.$$

Saat $x=6{,}3$, $7{,}5+h=8{,}7$.

**Jawab:** $\dot h=\dfrac{6{,}3}{8{,}7}(1{,}2)\approx0{,}87$ m/s.

@@ P1 | Latihan 1 | Laju luas lingkaran | geometri | 211
Jari-jari $r$ dan luas $A=\pi r^2$ berubah terhadap $t$. Tulis hubungan $dA/dt$ dengan $dr/dt$.
===
$$\frac{dA}{dt}=2\pi r\frac{dr}{dt}.$$

@@ P2 | Latihan 2 | Laju luas permukaan bola | geometri | 211
Tulis hubungan $dS/dt$ dengan $dr/dt$ untuk $S=4\pi r^2$.
===
$$\frac{dS}{dt}=8\pi r\frac{dr}{dt}.$$

@@ P3 | Latihan 3 | Hubungan linear | dasar | 211
$y=5x$ dan $dx/dt=2$. Tentukan $dy/dt$.
===
$\dot y=5\dot x=10$.

@@ P4 | Latihan 4 | Persamaan garis | dasar | 211
$2x+3y=12$ dan $dy/dt=-2$. Tentukan $dx/dt$.
===
$2\dot x+3\dot y=0\Rightarrow\dot x=3$.

@@ P5 | Latihan 5 | Parabola | dasar | 211
$y=x^2$, $dx/dt=3$. Tentukan $dy/dt$ saat $x=-1$.
===
$\dot y=2x\dot x=-6$.

@@ P6 | Latihan 6 | Fungsi kubik | dasar | 211
$x=y^3-y$, $dy/dt=5$. Tentukan $dx/dt$ saat $y=2$.
===
$\dot x=(3y^2-1)\dot y=55$.

@@ P7 | Latihan 7 | Lingkaran | dasar | 211
$x^2+y^2=25$, $dx/dt=-2$. Tentukan $dy/dt$ saat $x=3$, $y=-4$.
===
$\dot y=-\dfrac{x\dot x}{y}=-\dfrac{3(-2)}{-4}=-\dfrac32$.

@@ P8 | Latihan 8 | Kurva implisit | dasar | 211
$x^2y^3=\tfrac4{27}$, $dy/dt=\tfrac12$. Tentukan $dx/dt$ saat $x=2$.
===
Saat $x=2$, $y=\tfrac13$. Dari $2xy^3\dot x+3x^2y^2\dot y=0$ diperoleh $\dot x=-\dfrac{3x\dot y}{2y}=-\dfrac92$.

@@ P9 | Latihan 9 | Panjang vektor | dasar | 211
$L=\sqrt{x^2+y^2}$, $dx/dt=-1$, $dy/dt=3$. Tentukan $dL/dt$ saat $x=5$, $y=12$.
===
$\dot L=\dfrac{x\dot x+y\dot y}{L}=\dfrac{-5+36}{13}=\dfrac{31}{13}$.

@@ P10 | Latihan 10 | Tiga variabel | dasar | 211
$r+s^2+v^3=12$, $dr/dt=4$, $ds/dt=-3$. Tentukan $dv/dt$ saat $r=3$, $s=1$.
===
$v^3=8\Rightarrow v=2$. Dari $\dot r+2s\dot s+3v^2\dot v=0$: $4-6+12\dot v=0$, jadi $\dot v=\tfrac16$.

@@ P11 | Latihan 11 | Kubus mengecil | volume | 211
Rusuk kubus (semula 24 m) berkurang 5 m/menit. Saat rusuk 3 m, tentukan laju perubahan (a) luas permukaan dan (b) volume.
===
(a) $\dot S=12x\dot x=-180\ \text{m}^2$/menit.

(b) $\dot V=3x^2\dot x=-135\ \text{m}^3$/menit.

@@ P12 | Latihan 12 | Kubus membesar | volume | 211
Luas permukaan kubus bertambah $72\ \text{cm}^2$/s. Seberapa cepat volumenya berubah saat rusuk 3 cm?
===
$12x\dot x=72\Rightarrow\dot x=2$; $\dot V=3x^2\dot x=54\ \text{cm}^3$/s.

@@ P13 | Latihan 13 | Volume silinder | volume | 211
$V=\pi r^2h$. Hubungkan $dV/dt$ jika (a) $r$ tetap, (b) $h$ tetap, (c) keduanya berubah.
===
(a) $\dot V=\pi r^2\dot h$. (b) $\dot V=2\pi rh\thinspace \dot r$. (c) $\dot V=\pi r^2\dot h+2\pi rh\thinspace \dot r$.

@@ P14 | Latihan 14 | Volume kerucut | volume | 211
$V=\tfrac13\pi r^2h$. Jawab pertanyaan yang sama dengan latihan 13.
===
(a) $\dot V=\tfrac13\pi r^2\dot h$. (b) $\dot V=\tfrac23\pi rh\thinspace \dot r$. (c) $\dot V=\tfrac13\pi r^2\dot h+\tfrac23\pi rh\thinspace \dot r$.

@@ P17 | Latihan 17 | Jarak dua titik pada sumbu | laju | 211
$s=\sqrt{x^2+y^2}$ jarak antara $(x,0)$ dan $(0,y)$. Hubungkan lajunya jika (a) $y$ tetap, (b) keduanya berubah, (c) $s$ tetap.
===
(a) $\dot s=\dfrac{x\dot x}{s}$. (b) $\dot s=\dfrac{x\dot x+y\dot y}{s}$. (c) $\dot x=-\dfrac yx\dot y$.

@@ P18 | Latihan 18 | Diagonal balok | geometri | 211
$s=\sqrt{x^2+y^2+z^2}$. Hubungkan lajunya jika (a) semua berubah, (b) $x$ tetap, (c) $s$ tetap.
===
(a) $\dot s=\dfrac{x\dot x+y\dot y+z\dot z}{s}$. (b) $\dot s=\dfrac{y\dot y+z\dot z}{s}$. (c) $x\dot x+y\dot y+z\dot z=0$.

@@ P19 | Latihan 19 | Luas segitiga dengan sudut apit | geometri | 211
$A=\tfrac12ab\sin\theta$. Hubungkan $dA/dt$ jika (a) $a,b$ tetap, (b) hanya $b$ tetap, (c) semua berubah.
===
(a) $\dot A=\tfrac12ab\cos\theta\thinspace \dot\theta$.

(b) $\dot A=\tfrac12ab\cos\theta\thinspace \dot\theta+\tfrac12b\sin\theta\thinspace \dot a$.

(c) $\dot A=\tfrac12ab\cos\theta\thinspace \dot\theta+\tfrac12b\sin\theta\thinspace \dot a+\tfrac12a\sin\theta\thinspace \dot b$.

@@ P20 | Latihan 20 | Pelat logam dipanaskan | struktur | 211
Jari-jari pelat lingkaran bertambah 0,01 cm/menit karena pemanasan. Seberapa cepat luasnya bertambah saat jari-jari 50 cm?
===
$\dot A=2\pi r\dot r=\pi\ \text{cm}^2$/menit.

@@ P21 | Latihan 21 | Persegi panjang berubah | geometri | 211
Panjang $l$ berkurang 2 cm/s dan lebar $w$ bertambah 2 cm/s. Saat $l=12$, $w=5$ cm, tentukan laju (a) luas, (b) keliling, (c) diagonal. Mana yang naik atau turun?
===
(a) $\dot A=l\dot w+w\dot l=14\ \text{cm}^2$/s (naik).

(b) $\dot P=2(\dot l+\dot w)=0$ (tetap).

(c) $\dot d=\dfrac{12(-2)+5(2)}{13}=-\dfrac{14}{13}$ cm/s (turun).

@@ P22 | Latihan 22 | Balok tertutup berubah | geometri | 211
$\dot x=1$, $\dot y=-2$, $\dot z=1$ (m/s). Saat $x=4$, $y=3$, $z=2$, tentukan laju (a) volume, (b) luas permukaan, (c) diagonal.
===
(a) $\dot V=yz\dot x+xz\dot y+xy\dot z=6-16+12=2\ \text{m}^3$/s.

(b) $\dot S=2[(y+z)\dot x+(x+z)\dot y+(x+y)\dot z]=0$.

(c) $\dot s=\dfrac{4-6+2}{\sqrt{29}}=0$.

@@ P23 | Latihan 23 | Tangga merosot 3,9 m | struktur | 211–212
Tangga 3,9 m bersandar di rumah. Saat alasnya 3,6 m dari rumah, alas bergerak 1,5 m/s. (a) Seberapa cepat ujung atas merosot? (b) Laju luas segitiga? (c) Laju sudut tangga terhadap tanah?

{{fig:th_p23}}
===
Saat itu $y=\sqrt{3{,}9^2-3{,}6^2}=1{,}5$ m.

(a) $\dot y=-\dfrac{x\dot x}{y}=-3{,}6$ m/s (merosot 3,6 m/s).

(b) $\dot A=\tfrac12(\dot x y+x\dot y)=-5{,}355\ \text{m}^2$/s.

(c) Dari $\cos\theta=x/3{,}9$: $\dot\theta=-\dfrac{\dot x}{y}=-1$ rad/s.

@@ P24 | Latihan 24 | Dua pesawat menuju persimpangan lintasan | lintasan | 212
Dua pesawat terbang setinggi 12.000 m pada lintasan saling tegak lurus. $A$ mendekati titik potong dengan 442 knot, $B$ dengan 481 knot. Tentukan laju perubahan jarak saat $A$ 5 mil laut dan $B$ 12 mil laut dari titik potong.
===
Jarak $s=13$. $\dot s=\dfrac{5(-442)+12(-481)}{13}=-614$ knot: jarak berkurang 614 knot.

@@ P25 | Latihan 25 | Menerbangkan layang-layang | laju | 212
Layang-layang setinggi 90 m terbawa angin mendatar 7,5 m/s. Seberapa cepat benang harus diulur saat layang-layang 150 m dari pemegangnya?
===
$s^2=x^2+90^2$, saat $s=150$: $x=120$. $\dot s=\dfrac{x\dot x}{s}=\dfrac{120(7{,}5)}{150}=6$ m/s.

@@ P26 | Latihan 26 | Membubut lubang silinder | volume | 212
Silinder sedalam 15 cm diperbesar: jari-jari bertambah 0,001 cm setiap 3 menit. Seberapa cepat volume bertambah saat diameter 10 cm?
===
$V=15\pi r^2$, $\dot V=30\pi r\dot r=30\pi(5)\dfrac{0{,}001}{3}=0{,}05\pi\approx0{,}157\ \text{cm}^3$/menit.

@@ P27 | Latihan 27 | Timbunan pasir dari ban berjalan | struktur | 212
Pasir jatuh $10\ \text{m}^3$/menit ke puncak timbunan kerucut yang tingginya selalu $\tfrac38$ diameter alas. Tentukan laju (a) tinggi dan (b) jari-jari saat tinggi 4 m, dalam cm/menit.
===
$h=\tfrac34r$, sehingga $V=\dfrac{16\pi h^3}{27}$ dan $\dot V=\dfrac{16\pi h^2}{9}\dot h$.

(a) $\dot h=\dfrac{90}{256\pi}$ m/menit $\approx11{,}19$ cm/menit.

(b) $\dot r=\tfrac43\dot h\approx14{,}92$ cm/menit.

@@ P28 | Latihan 28 | Menguras kolam kerucut dangkal | air | 212
Air keluar $50\ \text{m}^3$/menit dari kolam beton kerucut (puncak di bawah) berjari-jari 45 m dan tinggi 6 m. Saat kedalaman 5 m, tentukan (a) laju turun muka air dan (b) laju perubahan jari-jari muka air.
===
$r=7{,}5h$, $V=18{,}75\pi h^3$, $\dot V=56{,}25\pi h^2\dot h$.

(a) $\dot h=-\dfrac{50}{1.406{,}25\pi}$ m/menit $\approx-1{,}13$ cm/menit.

(b) $\dot r=7{,}5\dot h\approx-8{,}49$ cm/menit.

@@ P29 | Latihan 29 | Menguras kolam setengah bola | air | 212
Air keluar $6\ \text{m}^3$/menit dari kolam setengah bola berjari-jari 13 m, $V=\tfrac\pi3y^2(3R-y)$. (a) Laju muka air saat kedalaman 8 m? (b) Jari-jari muka air saat kedalaman $y$? (c) Laju jari-jari itu saat $y=8$?

{{fig:th_p29}}
===
(a) $\dot V=\pi(26y-y^2)\dot y$. Saat $y=8$: $\dot y=-\dfrac{1}{24\pi}\approx-0{,}0133$ m/menit.

(b) $r=\sqrt{169-(13-y)^2}=\sqrt{26y-y^2}$.

(c) $\dot r=\dfrac{13-y}{r}\dot y$, saat $y=8$ ($r=12$): $\dot r=-\dfrac{5}{288\pi}\approx-0{,}0055$ m/menit.

@@ P30 | Latihan 30 | Tetes kabut membesar | volume | 212
Tetes berbentuk bola menyerap uap dengan laju sebanding luas permukaannya. Tunjukkan jari-jarinya bertambah dengan laju tetap.
===
$\dot V=kS$ berarti $4\pi r^2\dot r=k\thinspace 4\pi r^2$, sehingga $\dot r=k$ (tetap). $\blacksquare$

@@ P31 | Latihan 31 | Balon helium | volume | 212
Balon bola diisi $100\pi\ \text{m}^3$/menit. Saat jari-jari 5 m, tentukan laju jari-jari dan laju luas permukaan.
===
$4\pi(25)\dot r=100\pi\Rightarrow\dot r=1$ m/menit; $\dot S=8\pi r\dot r=40\pi\ \text{m}^2$/menit.

@@ P32 | Latihan 32 | Menarik sampan ke dermaga | lintasan | 212
Sampan ditarik dengan tali melalui cincin di dermaga 2 m di atas haluan. Tali ditarik 0,5 m/s. (a) Seberapa cepat sampan mendekat saat tali 3 m? (b) Laju sudut $\theta$ saat itu?

{{fig:th_p32}}
===
(a) $x=\sqrt{9-4}=\sqrt5$, $\dot x=\dfrac{L\dot L}{x}=-\dfrac{1{,}5}{\sqrt5}\approx-0{,}67$ m/s.

(b) $\cos\theta=2/L$ memberi $\dot\theta=\dfrac{2\dot L}{L^2\sin\theta}=-\dfrac{1}{3\sqrt5}\approx-0{,}149$ rad/s.

@@ P33 | Latihan 33 | Balon dan sepeda | lintasan | 212
Balon naik 0,3 m/s di atas jalan datar. Saat balon 20 m tingginya, sepeda berlaju 5 m/s melintas di bawahnya. Seberapa cepat jarak keduanya bertambah 3 s kemudian?

{{fig:th_p33}}
===
Saat itu $x=15$, $y=20{,}9$, $s=\sqrt{661{,}81}\approx25{,}73$.

$$\dot s=\frac{15(5)+20{,}9(0{,}3)}{s}\approx3{,}16\ \text{m/s}.$$

@@ P34 | Latihan 34 | Menyaring kopi (kerucut ke silinder) | air | 212–213
Cairan mengalir $160\ \text{cm}^3$/menit dari saringan kerucut (diameter 15 cm, tinggi 15 cm) ke wadah silinder berdiameter 15 cm. (a) Seberapa cepat muka di wadah naik saat kedalaman di kerucut 12 cm? (b) Seberapa cepat muka di kerucut turun?

{{fig:th_p34}}
===
(a) $\dot H=\dfrac{160}{\pi(7{,}5)^2}\approx0{,}905$ cm/menit.

(b) Di kerucut jari-jari muka $=h/2=6$ cm: laju turun $\dfrac{160}{36\pi}\approx1{,}41$ cm/menit.

@@ P36 | Latihan 36 | Sudut garis ke partikel pada parabola | gerak | 213
Partikel bergerak pada $y=x^2$ (kuadran I) dengan $\dot x=10$ m/s. Tentukan laju sudut garis ke titik asal saat $x=3$ m.
===
$\tan\theta=y/x=x$, sehingga $\dot\theta=\dfrac{\dot x}{1+x^2}=1$ rad/s.

@@ P37 | Latihan 37 | Jarak ke titik asal | gerak | 213
$\dot x=-1$ m/s, $\dot y=-5$ m/s. Tentukan laju perubahan jarak ke titik asal di $(5; 12)$.
===
$\dot D=\dfrac{5(-1)+12(-5)}{13}=-5$ m/s.

@@ P38 | Latihan 38 | Kamera mengikuti mobil balap | gerak | 213
Kamera berada 40 m dari lintasan; mobil melaju 80 m/s. Tentukan laju sudut kamera saat mobil tepat di depan dan 0,5 s kemudian.

{{fig:th_p38}}
===
Dengan $x=40\tan\theta$: $|\dot\theta|=\dfrac{40\thinspace |\dot x|}{40^2+x^2}$.

Tepat di depan ($x=0$): $2$ rad/s. Setelah 0,5 s ($x=40$): $1$ rad/s.

@@ P39 | Latihan 39 | Bayangan bola jatuh | gerak | 213
Lampu di puncak tiang 15 m. Bola dijatuhkan dari ketinggian sama, 9 m dari lampu, jatuh $s=4{,}9t^2$ m. Seberapa cepat bayangannya bergerak setelah $\tfrac12$ s?

{{fig:th_p39}}
===
Kesebangunan: $x=\dfrac{9(15)}{s}=\dfrac{135}{4{,}9t^2}$, $\dot x=-\dfrac{270}{4{,}9t^3}$.

**Jawab:** $\dot x\approx-440{,}8$ m/s (bergerak menuju tiang).

@@ P40 | Latihan 40 | Bayangan gedung | struktur | 213
Bayangan gedung 24 m panjangnya 18 m. Sudut matahari terhadap tanah bertambah $0{,}27^\circ$/menit. Seberapa cepat bayangan memendek (cm/menit)?

{{fig:th_p40}}
===
Misalkan $x$ panjang bayangan (m) dan $\theta$ sudut elevasi Matahari, yaitu sudut sinar Matahari terhadap tanah. Dari segitiga siku-siku, $\tan\theta=24/x$ atau $x=24\cot\theta$. Maka

$$\dot x=-24\csc^2\theta\thinspace \dot\theta.$$

Saat $x=18$: $\csc^2\theta=1+\left(\tfrac{18}{24}\right)^2=\tfrac{25}{16}$. Dalam radian, $\dot\theta=0{,}27\pi/180$ rad/menit.

$$\begin{aligned}\dot x&\approx-0{,}177\ \text{m/menit}\cr &=-17{,}7\ \text{cm/menit}.\end{aligned}$$

**Jawab:** bayangan memendek sekitar $17{,}7$ cm per menit.

@@ P41 | Latihan 41 | Lapisan es mencair | volume | 214
Bola besi berdiameter 8 cm dilapisi es yang mencair $10\ \text{cm}^3$/menit. Saat tebal es 2 cm, tentukan laju tebal es dan laju luas permukaan luar.
===
$V=\tfrac43\pi[(4+h)^3-64]$, $\dot V=4\pi(4+h)^2\dot h$.

$\dot h=-\dfrac{10}{144\pi}\approx-0{,}0221$ cm/menit. Luas luar $S=4\pi(4+h)^2$: $\dot S=48\pi\dot h=-\dfrac{10}{3}\ \text{cm}^2$/menit.

@@ P42 | Latihan 42 | Patroli udara jalan raya | lintasan | 214
Pesawat patroli terbang 3 km di atas jalan lurus dengan 120 km/jam. Saat jarak pandang ke mobil dari arah berlawanan 5 km dan berkurang 160 km/jam, berapa laju mobil?
===
Jarak mendatar $x=4$, $\dot x=\dfrac{s\dot s}{x}=-200$ km/jam. Itu jumlah kedua laju, sehingga mobil melaju $200-120=80$ km/jam.

@@ P43 | Latihan 43 | Pelari di lapangan bisbol | gerak | 214
Lapangan persegi bersisi 27 m. Pelari dari base 1 ke base 2 berlaju 5 m/s. (a) Laju jarak ke base 3 saat 9 m dari base 1? (b) Laju sudut $\theta_1,\theta_2$? (c) Saat menyentuh base 2 dengan 4,5 m/s?

{{fig:th_p43}}
===
Misalkan $z$ jarak ke base 2; saat itu $z=18$, $\dot z=-5$.

(a) $d=\sqrt{27^2+z^2}$, $\dot d=\dfrac{z\dot z}{d}\approx-2{,}77$ m/s.

(b) $\tan\theta_2=z/27$ dan $\theta_1=\tfrac\pi2-\theta_2$: $\dot\theta_2=\dfrac{27\dot z}{d^2}\approx-0{,}128$ rad/s, $\dot\theta_1\approx+0{,}128$ rad/s.

(c) $z=0$, $\dot z=-4{,}5$: $\dot\theta_1=\tfrac16$ rad/s dan $\dot\theta_2=-\tfrac16$ rad/s.

@@ P44 | Latihan 44 | Dua kapal bersudut 120° | lintasan | 214
Dua kapal menjauhi titik $O$ pada rute bersudut $120^\circ$, $A$ 14 knot dan $B$ 21 knot. Seberapa cepat mereka berpisah saat $OA=5$ dan $OB=3$ mil laut?
===
$d^2=a^2+b^2+ab\Rightarrow d=7$.

$$2d\dot d=2a\dot a+2b\dot b+\dot a\thinspace b+a\thinspace \dot b=413.$$

**Jawab:** $\dot d=29{,}5$ knot.

@@ P45 | Latihan 45 | Sudut jarum jam pukul 4 | gerak | 214
Dengan laju berapa sudut antara jarum menit dan jam berubah pada pukul 16.00?
===
Kecepatan sudut jarum menit $\omega_m=\pi/30$ rad/menit dan jarum jam $\omega_j=\pi/360$ rad/menit. Pukul 16.00 jarum menit di angka 12 dan jarum jam di angka 4, bersudut $120^\circ$. Jarum menit mengejar jarum jam, sehingga laju perubahan sudutnya adalah selisih kedua kecepatan sudut:

$$\begin{aligned}\dfrac{d\theta}{dt}&=\omega_j-\omega_m\cr &=\dfrac{\pi}{360}-\dfrac{\pi}{30}\cr &=-\dfrac{11\pi}{360}\ \text{rad/menit}.\end{aligned}$$

**Jawab:** sudut antara kedua jarum berkurang $5{,}5^\circ$ per menit.

@@ P46 | Latihan 46 | Tumpahan minyak berbentuk elips | air | 214
Lapisan minyak elips setebal 20 cm; sumbu panjang 2 km bertambah 9 m/jam, sumbu pendek $\tfrac34$ km bertambah 3 m/jam. Berapa debit minyak keluar?
===
$V=0{,}2\cdot\dfrac\pi4LW$, $\dot V=0{,}05\pi(\dot LW+L\dot W)=0{,}05\pi(9\cdot750+2.000\cdot3)$.

**Jawab:** $637{,}5\pi\approx2.003\ \text{m}^3$/jam.

@@ P47 | Latihan 47 | Sorot mercusuar di garis pantai | gerak | 214
Mercusuar 1 km lepas pantai berputar 3 kali per menit. Seberapa cepat titik sorot bergerak saat 1 km dari titik pantai terdekat?

{{fig:th_p47}}
===
$x=\tan\theta$, $\dot x=\sec^2\theta\thinspace \dot\theta=(2)(6\pi)$.

**Jawab:** $12\pi\approx37{,}7$ km/menit.
