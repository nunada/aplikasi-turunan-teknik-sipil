@@ C1 | Contoh 1 | Dua laju yang berkaitan | dasar | 152 (ed. 11)
$y=x^2+3$ dengan $x,y$ bergantung pada $t$. Tentukan $dy/dt$ saat $x=1$ jika $dx/dt=2$.
===
$\dot y=2x\dot x=4$.

@@ C2 | Contoh 2 | Riak air di kolam | air | 153 (ed. 11)
Jari-jari riak terluar bertambah 1 ft/s. Seberapa cepat luas permukaan yang terganggu bertambah saat jari-jari 4 ft?
===
$A=\pi r^2$, $\dot A=2\pi r\dot r=8\pi\ \text{ft}^2$/s.

@@ C3 | Contoh 3 | Balon mengembang | volume | 154 (ed. 11)
Balon bola dipompa $4{,}5\ \text{ft}^3$/menit. Tentukan laju jari-jari saat $r=2$ ft.
===
$\dot r=\dfrac{\dot V}{4\pi r^2}=\dfrac{9}{32\pi}\approx0{,}09$ ft/menit.

@@ C4 | Contoh 4 | Pesawat dipantau radar | gerak | 155 (ed. 11)
Pesawat terbang setinggi 6 mil menuju titik tepat di atas stasiun radar. Saat jarak $s=10$ mil, $s$ berkurang 400 mil/jam. Berapa laju pesawat?

{{fig:lr_c4}}
===
Misalkan $x$ jarak mendatar pesawat ke titik tepat di atas stasiun radar. Maka $x^2+6^2=s^2$, dan saat $s=10$ diperoleh $x=8$. Turunkan terhadap waktu dengan $\dot s=-400$:

$$\begin{aligned}\dot x&=\dfrac{s\thinspace \dot s}{x}=\dfrac{10(-400)}{8}\cr &=-500\ \text{mil/jam}.\end{aligned}$$

Tanda negatif menunjukkan bahwa jarak mendatar $x$ berkurang.

**Jawab:** pesawat mendekati titik tepat di atas stasiun radar dengan laju 500 mil/jam.

@@ C5 | Contoh 5 | Sudut elevasi kamera roket | gerak | 155 (ed. 11)
Roket naik dengan $s=50t^2$ ft. Kamera di tanah 2.000 ft dari landasan. Tentukan laju sudut elevasi pada $t=10$ s.

{{fig:lr_c5}}
===
Misalkan $\theta$ sudut elevasi kamera dan $s$ tinggi roket (ft). Kamera, landasan, dan roket membentuk segitiga siku-siku dengan sisi di depan $\theta$ sepanjang $s$ dan sisi di sampingnya $2.000$ ft, sehingga

$$\tan\theta=\dfrac{s}{2.000}.$$

Turunkan terhadap waktu, lalu gunakan $\cos^2\theta=\dfrac{2.000^2}{s^2+2.000^2}$:

$$\dot\theta=\dfrac{2.000\thinspace \dot s}{s^2+2.000^2}.$$

Saat $t=10$: $s=50(10)^2=5.000$ ft dan $\dot s=100t=1.000$ ft/s.

**Jawab:** sudut elevasi kamera bertambah dengan laju $\dot\theta=\dfrac{2}{29}\approx0{,}069$ rad/s.

@@ C6 | Contoh 6 | Kecepatan piston | gerak | 156
Batang penghubung 7 inci dipasang pada engkol berjari-jari 3 inci yang berputar 200 putaran/menit berlawanan jarum jam. Tentukan kecepatan piston saat $\theta=\pi/3$.

{{fig:lr_c6}}
===
Aturan kosinus: $49=9+x^2-6x\cos\theta$. Turunkan dengan $\dot\theta=400\pi$:

$$\dot x=\frac{6x\sin\theta}{6\cos\theta-2x}\thinspace \dot\theta.$$

Saat $\theta=\pi/3$, $x=8$.

**Jawab:** $\dot x=-\dfrac{9.600\pi\sqrt3}{13}\approx-4.018$ inci/menit.

@@ P1 | Latihan 1 | Persamaan laju berkaitan | dasar | 157
Apa yang dimaksud persamaan laju yang berkaitan?
===
Persamaan yang menghubungkan turunan terhadap waktu dari beberapa besaran, diperoleh dengan menurunkan secara implisit persamaan yang menghubungkan besaran-besaran itu.

@@ P2 | Latihan 2 | Langkah penyelesaian | dasar | 157
Sebutkan panduan menyelesaikan soal laju yang berkaitan.
===
- Tentukan yang diketahui dan ditanyakan, lalu buat sketsa berlabel.
- Tulis persamaan yang menghubungkan variabel-variabel yang lajunya diketahui atau dicari.
- Turunkan kedua ruas terhadap $t$ dengan aturan rantai.
- Setelah itu baru substitusikan nilai sesaat, lalu selesaikan laju yang dicari.

@@ P3 | Latihan 3 | Fungsi akar | dasar | 157
$y=\sqrt x$. (a) $\dot y$ saat $x=4$, $\dot x=3$. (b) $\dot x$ saat $x=25$, $\dot y=2$.
===
$\dot y=\dfrac{\dot x}{2\sqrt x}$. (a) $\tfrac34$. (b) $20$.

@@ P4 | Latihan 4 | Fungsi kuadrat | dasar | 157
$y=3x^2-5x$. (a) $\dot y$ saat $x=3$, $\dot x=2$. (b) $\dot x$ saat $x=2$, $\dot y=4$.
===
$\dot y=(6x-5)\dot x$. (a) $26$. (b) $\tfrac47$.

@@ P5 | Latihan 5 | Hiperbola | dasar | 157
$xy=4$. (a) $\dot y$ saat $x=8$, $\dot x=10$. (b) $\dot x$ saat $x=1$, $\dot y=-6$.
===
$y\dot x+x\dot y=0$. (a) $-\tfrac58$. (b) $\tfrac32$.

@@ P6 | Latihan 6 | Lingkaran | dasar | 157
$x^2+y^2=25$. (a) $\dot y$ di $(3; 4)$, $\dot x=8$. (b) $\dot x$ di $(4; 3)$, $\dot y=-2$.
===
$x\dot x+y\dot y=0$. (a) $-6$. (b) $\tfrac32$.

@@ P7 | Latihan 7 | Titik pada parabola | gerak | 157
$y=2x^2+1$, $\dot x=2$ cm/s. Tentukan $\dot y$ di $x=-1; 0; 1$.
===
$\dot y=4x\dot x=8x$: $-8$, $0$, $8$ cm/s.

@@ P8 | Latihan 8 | Titik pada kurva rasional | gerak | 157
$y=\dfrac{1}{1+x^2}$, $\dot x=6$ inci/s. Tentukan $\dot y$ di $x=-2; 0; 2$.
===
$\dot y=-\dfrac{12x}{(1+x^2)^2}$: $\tfrac{24}{25}$, $0$, $-\tfrac{24}{25}$ inci/s.

@@ P9 | Latihan 9 | Titik pada kurva tangen | gerak | 157
$y=\tan x$, $\dot x=3$ ft/s. Tentukan $\dot y$ di $x=-\pi/3; -\pi/4; 0$.
===
$\dot y=3\sec^2x$: $12$, $6$, $3$ ft/s.

@@ P10 | Latihan 10 | Titik pada kurva kosinus | gerak | 157
$y=\cos x$, $\dot x=4$ cm/s. Tentukan $\dot y$ di $x=\pi/6; \pi/4; \pi/3$.
===
$\dot y=-4\sin x$: $-2$, $-2\sqrt2$, $-2\sqrt3$ cm/s.

@@ P11 | Latihan 11 | Luas lingkaran | geometri | 157
Jari-jari bertambah 4 cm/menit. Tentukan laju luas saat $r=37$ cm.
===
$\dot A=2\pi(37)(4)=296\pi\ \text{cm}^2$/menit.

@@ P12 | Latihan 12 | Luas segitiga sama sisi | geometri | 157
Sisi bertambah 13 ft/jam. Tentukan laju luas saat $s=41$ ft.
===
$\dot A=\dfrac{\sqrt3}{2}s\dot s=\dfrac{533\sqrt3}{2}\approx461{,}6\ \text{ft}^2$/jam.

@@ P13 | Latihan 13 | Volume bola | volume | 157
$r$ bertambah 3 inci/menit. (a) Laju volume saat $r=9$ dan $r=36$ inci. (b) Mengapa tidak tetap?
===
(a) $\dot V=12\pi r^2$: $972\pi$ dan $15.552\pi\ \text{inci}^3$/menit.

(b) $\dot V$ bergantung pada $r^2$, padahal $r$ berubah.

@@ P14 | Latihan 14 | Jari-jari balon | volume | 157
Balon diisi $800\ \text{cm}^3$/menit. (a) Laju jari-jari saat $r=30$ dan 85 cm. (b) Mengapa tidak tetap?
===
(a) $\dot r=\dfrac{200}{\pi r^2}$: $\dfrac{2}{9\pi}\approx0{,}071$ dan $\dfrac{8}{289\pi}\approx0{,}0088$ cm/menit.

(b) Luas permukaan bertambah, sehingga volume tambahan yang sama menjadi lapisan yang makin tipis.

@@ P15 | Latihan 15 | Volume kubus | volume | 157
Rusuk bertambah 6 cm/s. Tentukan laju volume saat rusuk 2 cm dan 10 cm.
===
$\dot V=18x^2$: $72$ dan $1.800\ \text{cm}^3$/s.

@@ P16 | Latihan 16 | Luas permukaan kubus | geometri | 157
Seperti latihan 15, tentukan laju luas permukaan.
===
$\dot S=12x\dot x=72x$: $144$ dan $720\ \text{cm}^2$/s.

@@ P17 | Latihan 17 | Timbunan pasir dan kerikil | struktur | 157
Pasir jatuh $10\ \text{ft}^3$/menit; diameter alas timbunan kerucut sekitar tiga kali tingginya. Tentukan laju tinggi saat 15 ft.
===
$r=1{,}5h$, $V=0{,}75\pi h^3$, $\dot h=\dfrac{\dot V}{2{,}25\pi h^2}=\dfrac{8}{405\pi}\approx0{,}0063$ ft/menit.

@@ P18 | Latihan 18 | Minyak dalam wadah silinder | volume | 157
Volume minyak bertambah $150\ \text{inci}^3$/s. Tinggi silinder sekitar sepuluh kali jari-jarinya. Tentukan laju tinggi minyak saat 35 inci.
===
Soal ini dimaksudkan memakai $r=h/10$, sehingga $V=\dfrac{\pi h^3}{100}$:

$$\dot h=\frac{100\thinspace \dot V}{3\pi h^2}=\frac{200}{49\pi}\approx1{,}30\ \text{inci/s}.$$

**Catatan:** untuk wadah silinder tegak yang nyata, jari-jari minyak tetap sehingga $\dot h=\dot V/(\pi r^2)$ konstan. Redaksi soal perlu diperjelas bila dipakai sebagai tugas.

@@ P19 | Latihan 19 | Mengisi kolam renang berdasar miring | air | 157
Kolam panjang 12 m, lebar 6 m, dalam 1 m di ujung dangkal dan 3 m di ujung dalam, diisi $\tfrac14\ \text{m}^3$/menit. Kedalaman air di ujung dalam 1 m. (a) Berapa persen terisi? (b) Laju muka air?

{{fig:lr_p19}}
===
Untuk kedalaman $h\le2$, penampang air segitiga dengan panjang $6h$: $V=\tfrac12h(6h)(6)=18h^2$.

(a) Volume kolam $144\ \text{m}^3$; terisi $\dfrac{18}{144}=0{,}125$, yaitu 12,5%.

(b) $36h\dot h=\tfrac14\Rightarrow\dot h=\dfrac{1}{144}$ m/menit.

@@ P20 | Latihan 20 | Palung segitiga | air | 158
Palung panjang 12 ft, lebar atas 3 ft, tinggi penampang segitiga 3 ft. (a) Diisi $2\ \text{ft}^3$/menit, laju muka air saat $h=1$ ft? (b) Muka naik $\tfrac38$ inci/menit saat $h=2$ ft, berapa debitnya?

{{fig:lr_p20}}
===
Lebar muka $=h$, $V=6h^2$, $\dot V=12h\dot h$.

(a) $\dot h=\tfrac16$ ft/menit.

(b) $\dot h=\tfrac1{32}$ ft/menit, $\dot V=\tfrac34\ \text{ft}^3$/menit.

@@ P21 | Latihan 21 | Tangga 25 ft | struktur | 158
Tangga 25 ft; alasnya ditarik menjauhi dinding 2 ft/s. (a) Laju ujung atas saat alas 7, 15, 24 ft. (b) Laju luas segitiga saat alas 7 ft. (c) Laju sudut tangga terhadap dinding saat itu.

{{fig:lr_p21}}
===
(a) $\dot y=-\dfrac{2x}{y}$: $-\tfrac{7}{12}$, $-\tfrac32$, $-\tfrac{48}{7}$ ft/s.

(b) $\dot A=\tfrac12(\dot xy+x\dot y)=\dfrac{527}{24}\approx21{,}96\ \text{ft}^2$/s.

(c) $\sin\theta=x/25$, $\dot\theta=\dfrac{\dot x}{y}=\tfrac1{12}$ rad/s.

@@ P22 | Latihan 22 | Menaikkan papan ke gedung | struktur | 158
Papan 5 m ditarik naik sepanjang dinding dengan tali 0,15 m/s; ujung bawah meluncur di tanah. Seberapa cepat ujung bawah meluncur saat 2,5 m dari dinding?

{{fig:lr_p22}}
===
$x^2+y^2=25$, $y=\sqrt{18{,}75}$, $\dot y=0{,}15$:

$$\dot x=-\frac{y\dot y}{x}\approx-0{,}26\ \text{m/s (menuju dinding)}.$$

@@ P23 | Latihan 23 | Menegakkan pipa dengan winch | struktur | 158
Winch di puncak gedung 12 m menegakkan pipa 12 m yang berporos di dasar gedung. Tali ditarik dengan $ds/dt=-0{,}2$ m/s. Tentukan laju vertikal dan horizontal ujung pipa saat $y=6$ m.

{{fig:lr_p23}}
===
$s^2=x^2+(12-y)^2=288-24y$. Saat $y=6$, $s=12$:

$$\dot y=-\frac{s\dot s}{12}=0{,}2\ \text{m/s}.$$

Dari $x^2+y^2=144$: $\dot x=-\dfrac{y\dot y}{x}=-\dfrac{\sqrt3}{15}\approx-0{,}115$ m/s.

@@ P24 | Latihan 24 | Winch dan perahu | lintasan | 158
Winch 12 ft di atas geladak. (a) Tali ditarik 4 ft/s; laju perahu saat tali 13 ft? Bagaimana saat mendekat? (b) Perahu bergerak tetap 4 ft/s; laju tarik winch saat tali 13 ft?

{{fig:lr_p24}}
===
$x^2+144=L^2$, saat $L=13$, $x=5$.

(a) $\dot x=\dfrac{L\dot L}{x}=-10{,}4$ ft/s. Laju membesar tanpa batas saat $x\to0$.

(b) $\dot L=\dfrac{x\dot x}{L}=-\dfrac{20}{13}\approx-1{,}54$ ft/s. Laju tarik mengecil menuju nol.

@@ P25 | Latihan 25 | Pengatur lalu lintas udara | lintasan | 158
Dua pesawat setinggi sama menuju satu titik pada lintasan tegak lurus: 225 mil dengan 450 mil/jam dan 300 mil dengan 600 mil/jam. (a) Laju berkurangnya jarak? (b) Waktu tersedia untuk mengubah lintasan?

{{fig:lr_p25}}
===
(a) $s=375$, $\dot s=\dfrac{225(-450)+300(-600)}{375}=-750$ mil/jam.

(b) Keduanya tiba bersamaan dalam $0{,}5$ jam: **30 menit**.

@@ P26 | Latihan 26 | Pesawat di atas antena radar | gerak | 158
Pesawat setinggi 5 mil. Saat $s=10$ mil, radar mencatat $s$ berubah 240 mil/jam. Berapa laju pesawat?

{{fig:lr_p26}}
===
$x=\sqrt{75}$, $\dot x=\dfrac{s\dot s}{x}=160\sqrt3\approx277$ mil/jam.

@@ P27 | Latihan 27 | Pelari menuju base ketiga | gerak | 159
Lapangan persegi sisi 90 ft. Pelari dari base 2 ke 3 berlaju 25 ft/s; saat 20 ft dari base 3, tentukan laju jaraknya ke home.

{{fig:lr_p27}}
===
$d=\sqrt{90^2+20^2}$, $\dot d=\dfrac{20(-25)}{d}\approx-5{,}42$ ft/s.

@@ P28 | Latihan 28 | Pelari menuju base kedua | gerak | 159
Pada lapangan latihan 27, pelari dari base 1 ke 2 (25 ft/s), 20 ft dari base 2. Tentukan laju jaraknya ke home.
===
Jarak dari base 1 adalah 70 ft: $\dot d=\dfrac{70(25)}{\sqrt{90^2+70^2}}\approx15{,}35$ ft/s.

@@ P29 | Latihan 29 | Bayangan menjauhi lampu | laju | 159
Mahasiswa 6 ft menjauhi lampu 15 ft dengan 5 ft/s. Saat 10 ft dari tiang: (a) laju ujung bayangan; (b) laju panjang bayangan.

{{fig:lr_p29}}
===
Ujung bayangan $X=\tfrac53x$. (a) $\dot X=\tfrac{25}{3}$ ft/s. (b) Panjang $X-x=\tfrac23x$: $\tfrac{10}{3}$ ft/s.

@@ P30 | Latihan 30 | Bayangan mendekati lampu | laju | 159
Ulangi latihan 29 untuk mahasiswa yang mendekati lampu 20 ft.

{{fig:lr_p30}}
===
$X=\tfrac{10}{7}x$, $\dot x=-5$. (a) $\dot X=-\tfrac{50}{7}$ ft/s. (b) Panjang $\tfrac37x$: $-\tfrac{15}{7}$ ft/s.

@@ P31 | Latihan 31 | Batang mesin berpeluncur | gerak | 159
Ujung batang 1 m berada di $(x,0)$ dan $(0,y)$ dengan $x(t)=\tfrac12\sin(\pi t/6)$. (a) Periode? (b) Titik terendah ujung di sumbu-$y$? (c) Laju ujung sumbu-$y$ saat $x=\tfrac14$?

{{fig:lr_p31}}
===
(a) $12$ s. (b) $y=\sqrt{1-x^2}$ minimum saat $|x|=\tfrac12$: $y=\dfrac{\sqrt3}{2}$.

(c) $|\dot x|=\dfrac{\pi\sqrt3}{24}$, $|\dot y|=\dfrac{x}{y}|\dot x|=\dfrac{\sqrt5\thinspace \pi}{120}\approx0{,}059$ m/s.

@@ P32 | Latihan 32 | Batang mesin, gerak lain | gerak | 159
Ulangi latihan 31 untuk $x(t)=\tfrac35\sin\pi t$, bagian (c) di $x=\tfrac3{10}$.
===
(a) $2$ s. (b) $y_{\min}=\tfrac45$.

(c) $|\dot x|=\dfrac{3\sqrt3\thinspace \pi}{10}$, $y=\dfrac{\sqrt{91}}{10}$, $|\dot y|=\dfrac{9\sqrt3\thinspace \pi}{10\sqrt{91}}\approx0{,}51$ m/s.

@@ P33 | Latihan 33 | Tetes hujan menguap | volume | 159
Tetes bola menguap dengan laju sebanding luas permukaannya. Tunjukkan jari-jarinya berkurang dengan laju tetap.
===
$4\pi r^2\dot r=-k\thinspace 4\pi r^2\Rightarrow\dot r=-k$. $\blacksquare$

@@ P34 | Latihan 34 | Tanda laju dari grafik | dasar | 159
Dari kedua grafik, tentukan (a) tanda $dy/dt$ bila $dx/dt<0$; (b) tanda $dx/dt$ bila $dy/dt>0$.

{{fig:lr_p34a lr_p34b}}
===
Berlaku $\dot y=f'(x)\thinspace \dot x$.

(i) $f$ turun ($f'<0$): (a) $\dot y>0$; (b) $\dot x<0$.

(ii) $f$ naik ($f'>0$): (a) $\dot y<0$; (b) $\dot x>0$.

@@ P35 | Latihan 35 | Makna persamaan laju | dasar | 159
Jelaskan hubungan $\dot y$ dan $\dot x$ pada (a) $\dot y=3\dot x$ dan (b) $\dot y=x(L-x)\dot x$, $0\le x\le L$ (semua laju positif).
===
(a) $\dot y$ selalu tiga kali $\dot x$.

(b) Faktor pengali bergantung pada posisi: nol di $x=0$ dan $x=L$, terbesar ($L^2/4$) di $x=L/2$.

@@ P36 | Latihan 36 | Laju volume kubus | dasar | 159
Jika $ds/dt$ tetap, bagaimana $dV/dt$ berubah?
===
$\dot V=3s^2\dot s$ tidak tetap; sebanding dengan $s^2$.

@@ P39 | Latihan 39 | Pesawat menanjak | gerak | 159
Pesawat berlaju udara 275 mil/jam menanjak $18^\circ$ di udara tenang. Tentukan laju pertambahan ketinggian.
===
$\dot h=275\sin18^\circ\approx85{,}0$ mil/jam.

@@ P40 | Latihan 40 | Sudut elevasi balon | gerak | 159
Balon naik 4 m/s dari titik 50 m dari pengamat. Tentukan laju sudut elevasi saat tinggi 50 m.
===
$\dot\theta=\dfrac{50\thinspace \dot h}{50^2+h^2}=\dfrac{200}{5.000}=0{,}04$ rad/s.

@@ P41 | Latihan 41 | Menggulung tali pancing | gerak | 160
Ujung joran 10 ft di atas air. Tali digulung 1 ft/s. Tentukan laju sudut tali terhadap air saat panjang tali 25 ft.

{{fig:lr_p41}}
===
Laju 1 ft/s dipakai untuk panjang tali $L$. $\sin\theta=10/L$:

$$\dot\theta=-\frac{10\dot L}{L^2\cos\theta}=\frac{10}{625\cos\theta}\approx0{,}0175\ \text{rad/s}.$$

@@ P42 | Latihan 42 | Sudut elevasi pesawat | gerak | 160
Pesawat setinggi 5 mil terbang 600 mil/jam menuju titik di atas pengamat. Tentukan laju sudut saat $\theta=30^\circ,60^\circ,75^\circ$.

{{fig:lr_p42}}
===
$x=5\cot\theta$, $\dot x=-600$, sehingga $\dot\theta=120\sin^2\theta$ rad/jam: $30$, $90$, dan $\approx112$ rad/jam.

@@ P43 | Latihan 43 | Sorot lampu mobil patroli | gerak | 160
Mobil 50 ft dari gudang panjang; lampunya berputar 30 putaran/menit. Tentukan laju sorot di dinding saat $\theta=30^\circ,60^\circ,70^\circ$.

{{fig:lr_p43}}
===
$x=50\tan\theta$, $\dot x=50\sec^2\theta\thinspace (60\pi)=\dfrac{3.000\pi}{\cos^2\theta}$ ft/menit: $\approx12.566$; $37.699$; $80.569$ ft/menit.

@@ P44 | Latihan 44 | Titik pada roda berputar | gerak | 160
Roda berjari-jari 30 cm berputar 10 putaran/s. (a) $dx/dt$ sebagai fungsi $\theta$. (b) Grafik. (c) Kapan $|dx/dt|$ terbesar dan terkecil? (d) Nilai di $30^\circ$ dan $60^\circ$.

{{fig:lr_p44}}
===
(a) $x=30\cos\theta$, $\dot\theta=20\pi$: $\dot x=-600\pi\sin\theta$ cm/s (dengan $\theta$ bertambah terhadap waktu).

(b)

{{fig:lr_p44g}}

(c) Terbesar di $\theta=90^\circ,270^\circ$; terkecil (nol) di $0^\circ,180^\circ$.

(d) $-300\pi$ dan $-300\sqrt3\thinspace \pi$ cm/s.

@@ P45 | Latihan 45 | Segitiga sama kaki | geometri | 160
Panjang kedua sisi yang sama, $s$, **tetap**, sedangkan sudut apitnya $\theta$ berubah. (a) Tunjukkan $A=\tfrac12s^2\sin\theta$. (b) $\dot\theta=\tfrac12$ rad/menit; laju luas saat $\theta=\pi/6$ dan $\pi/3$.
===
(a) Alas $s$, tinggi $s\sin\theta$, jadi $A=\tfrac12s^2\sin\theta$.

(b) Karena $s$ tetap ($\dot s=0$): $\dot A=\tfrac12s^2\cos\theta\thinspace \dot\theta=\dfrac{s^2\cos\theta}{4}$, sehingga lajunya $\dfrac{\sqrt3}{8}s^2$ dan $\dfrac{s^2}{8}$ (satuan luas per menit).

**Catatan:** jika $s$ ikut berubah, turunannya memuat suku tambahan $s\thinspace \dot s\sin\theta$.

@@ P46 | Latihan 46 | Kamera pengawas koridor | struktur | 160
Kamera 50 ft di atas lantai menyapu koridor 100 ft dengan pusat fokus bergerak $|dx/dt|=2$ ft/s. Buat model laju putarnya.

{{fig:lr_p46}}
===
$x=50\tan\theta$, sehingga $|\dot\theta|=\dfrac{2\cos^2\theta}{50}=\dfrac{\cos^2\theta}{25}=\dfrac{100}{x^2+2.500}$ rad/s, $-50\le x\le50$.

@@ P48 | Latihan 48 | Bayangan bola dan tiang lampu | gerak | 160
Bola dijatuhkan dari ketinggian 20 m, 12 m dari puncak tiang lampu 20 m. Seberapa cepat bayangannya bergerak 1 s setelah dilepas?
===
$x=\dfrac{12(20)}{4{,}9t^2}$, $\dot x=-\dfrac{480}{4{,}9t^3}\approx-98{,}0$ m/s.

@@ P49 | Latihan 49 | Percepatan ujung tangga | gerak | 160
Tentukan percepatan ujung atas tangga latihan 21 saat alas 7 ft dari dinding.
===
Turunkan $x\dot x+y\dot y=0$ dengan $\ddot x=0$: $\dot x^2+\dot y^2+y\ddot y=0$.

$$\ddot y=-\frac{4+49/144}{24}=-\frac{625}{3.456}\approx-0{,}181\ \text{ft/s}^2.$$

@@ P50 | Latihan 50 | Percepatan perahu | gerak | 160
Tentukan percepatan perahu latihan 24(a) saat tali 13 ft.
===
Turunkan $x\dot x=L\dot L$ dengan $\ddot L=0$: $\dot x^2+x\ddot x=\dot L^2$.

$$\ddot x=\frac{16-108{,}16}{5}\approx-18{,}43\ \text{ft/s}^2.$$
