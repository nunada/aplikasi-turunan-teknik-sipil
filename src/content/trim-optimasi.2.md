@@ P41 | Latihan 41 | Balok terpanjang melewati sudut koridor | struktur | 289
Dua koridor selebar 3 m dan 6 m bertemu siku. Cari panjang balok terpanjang yang dapat dibawa horizontal melewati sudut (ukuran penampang diabaikan).

{{fig:t_p41}}
===
$L(\theta)=\dfrac{3}{\cos\theta}+\dfrac{6}{\sin\theta}$. Balok terpanjang = minimum $L$, saat $\tan^3\theta=2$.

**Jawab:** $\left(3^{2/3}+6^{2/3}\right)^{3/2}\approx12{,}49$ m.

@@ P42 | Latihan 42 | Balok berpenampang persegi di sudut koridor | struktur | 289
Ulangi latihan 41 dengan balok berpenampang persegi bersisi $\tfrac13$ m.

{{fig:t_p42}}
===
Sisi luar balok menyentuh kedua dinding luar, sisi dalam menyentuh sudut:

$$L(\theta)=\frac{3}{\cos\theta}+\frac{6}{\sin\theta}-\frac{1/3}{\sin\theta\cos\theta}.$$

$L'=0$ diselesaikan numerik: $\theta\approx0{,}908$.

**Jawab:** panjang maksimum $\approx11{,}80$ m.

@@ P44 | Latihan 44 | Ekstrem dengan parameter | dasar | 289
Cari ekstrem mutlak $f(x)=\dfrac{x}{x^2+c}$ pada $0\le x\le c$ dengan $c>1$.
===
$f'=\dfrac{c-x^2}{(x^2+c)^2}$, titik kritis $x=\sqrt c<c$. $f(0)=0$, $f(c)=\dfrac1{c+1}>0$.

**Jawab:** minimum $0$, maksimum $\dfrac{1}{2\sqrt c}$.

@@ P45 | Latihan 45 | Waktu optimum mengganti mesin | biaya | 289
Biaya tahunan mesin yang disimpan $t$ tahun: $C(t)=\dfrac pt+\dfrac{nr}{t}$ dengan jumlah perbaikan $n=t^\alpha/\beta$ ($\alpha>1$). (a) Kapan diganti? (b) Bahas $\alpha=1$ dan $0<\alpha<1$.
===
(a) $C=\dfrac pt+\dfrac{r}{\beta}t^{\alpha-1}$,

$$C'=-\frac{p}{t^2}+\frac{r(\alpha-1)}{\beta}t^{\alpha-2}=0\Rightarrow t=\left[\frac{p\beta}{r(\alpha-1)}\right]^{1/\alpha}.$$

(b) Untuk $\alpha\le1$, $C'<0$ selalu: biaya tahunan terus turun, jadi secara model mesin **tidak perlu diganti**.

@@ P46 | Latihan 46 | Penerangan minimum dua sumber | struktur | 289
Dua sumber berintensitas $I_1$ dan $I_2$ berjarak $d$. Di titik mana pada ruas penghubung penerangan total minimum?
===
$x$ dari $I_1$: $E=k\left(\dfrac{I_1}{x^2}+\dfrac{I_2}{(d-x)^2}\right)$, $E'=0\Rightarrow\dfrac{I_1}{x^3}=\dfrac{I_2}{(d-x)^3}$.

**Jawab:** $x=\dfrac{d\,\sqrt[3]{I_1}}{\sqrt[3]{I_1}+\sqrt[3]{I_2}}$.

@@ P47 | Latihan 47 | Proporsi jendela dua jenis kaca | struktur | 289
Jendela persegi panjang beratap setengah lingkaran; kaca berwarna meneruskan setengah cahaya kaca bening; keliling tetap. Cari proporsi terbaik.

{{fig:t_win}}
===
Jari-jari $r$, tinggi $h$, $P=2r+2h+\pi r$. Cahaya $\propto 2rh+\dfrac{\pi r^2}{4}=Pr-2r^2-\dfrac{3\pi r^2}{4}$, maksimum di $r=\dfrac{2P}{8+3\pi}$, lalu $h=\dfrac{(4+\pi)P}{2(8+3\pi)}$.

**Jawab:** $\dfrac{2r}{h}=\dfrac{8}{4+\pi}$.

@@ P48 | Latihan 48 | Tangki 100 m³ dengan biaya material dan las | biaya | 289
Tangki balok beralas persegi bervolume $100\ \text{m}^3$. (a) Dinding dan atap 1,25 dolar/m², alas 4,75 dolar/m². Cari dimensi termurah. (b) Tambahkan biaya las 7,50 dolar/m pada 12 rusuk.
===
$h=100/x^2$.

(a) $C=6x^2+\dfrac{500}{x}$, $C'=0\Rightarrow x^3=\dfrac{125}{3}$.

**Jawab:** $x\approx3{,}47$ m, $h\approx8{,}32$ m ($C\approx216$ dolar).

(b) 8 rusuk sepanjang $x$ dan 4 sepanjang $h$:

$$C=6x^2+\frac{500}{x}+60x+\frac{3000}{x^2}.$$

$C'=0\iff3x^4+15x^3-125x-1500=0$, numerik $x\approx4{,}19$.

**Jawab:** $x\approx4{,}19$ m, $h\approx5{,}71$ m.

@@ P49 | Latihan 49 | Estimasi kemungkinan maksimum | dasar | 289
Fungsi likelihood dadu: $f(x)=\dfrac{n!}{m!(n-m)!}x^m(1-x)^{n-m}$, $0\le x\le1$. Tunjukkan maksimumnya di $x=m/n$.
===
Untuk $0<m<n$:

$$f'(x)\propto x^{m-1}(1-x)^{n-m-1}(m-nx)=0\Rightarrow x=\frac mn.$$

$f(0)=f(1)=0$ dan $f>0$ di dalam, jadi ini maksimum. Untuk $m=0$ atau $m=n$, maksimum di ujung yang juga sama dengan $m/n$. $\blacksquare$

@@ P50 | Latihan 50 | Trase pipa melintasi dua jenis tanah | biaya | 289
Pipa bawah tanah dari $A$ ke $B$ melintasi daerah I (biaya $c_1$/km) dan II ($c_2$/km). Tunjukkan biaya minimum saat $c_1\sin\theta_1=c_2\sin\theta_2$.

{{fig:t_p50}}
===
$$C(x)=c_1\sqrt{x^2+y_1^2}+c_2\sqrt{(x_2-x)^2+y_2^2}.$$

$$C'=c_1\frac{x}{\sqrt{x^2+y_1^2}}-c_2\frac{x_2-x}{\sqrt{(x_2-x)^2+y_2^2}}=c_1\sin\theta_1-c_2\sin\theta_2=0.$$

$C''>0$, sehingga titik tersebut minimum. $\blacksquare$

@@ P51 | Latihan 51 | Saat terakhir mencegat kapal selam | lintasan | 289
Kapal selam bergerak ke timur $s$ km/jam dan melintas 1 km di utara suatu titik pulau tepat tengah malam. Rakit dari titik itu berlaju $v<s$. Kapan paling lambat rakit harus berangkat?
===
Berangkat pada $T$, bertemu pada $t$: $v(t-T)=\sqrt{s^2t^2+1}$, jadi

$$T(t)=t-\frac{\sqrt{s^2t^2+1}}{v}.$$

$T'=0\Rightarrow t=\dfrac{v}{s\sqrt{s^2-v^2}}$, dan nilainya $T=-\dfrac{\sqrt{s^2-v^2}}{sv}$.

**Jawab:** $\dfrac{\sqrt{s^2-v^2}}{sv}$ jam **sebelum** tengah malam.

@@ P52 | Latihan 52 | Kotak kemasan dari karton 1 m × 2 m | volume | 290
Karton $1\times2$ m dipotong dan dilipat menjadi kotak seperti gambar. Sayap luar atas dan bawah harus bertemu di tengah; sayap dalam tidak harus. Cari kotak bervolume terbesar dan jarak antar sayap dalam.

{{fig:t_p52a t_p52b}}
===
$2l+2w=2\Rightarrow l=1-w$. Sayap luar selebar $w/2$ atas dan bawah, jadi $h=1-w$.

$$V=lwh=w(1-w)^2,\quad V'=(1-w)(1-3w)=0\Rightarrow w=\tfrac13.$$

**Jawab:** $l=h=\tfrac23$ m, $w=\tfrac13$ m, $V=\tfrac4{27}\ \text{m}^3$; sayap dalam berjarak $l-w=\tfrac13$ m.

@@ P53 | Latihan 53 | Kecepatan kapal paling ekonomis | biaya | 290
Biaya bahan bakar per jam sebanding dengan pangkat tiga laju, bernilai $B$ dolar pada $b$ km/jam; biaya tetap $A$ dolar/jam. Cari laju paling hemat.
===
Biaya per km: $c(v)=\dfrac Av+\dfrac{Bv^2}{b^3}$, $c'=0\Rightarrow v^3=\dfrac{Ab^3}{2B}$.

**Jawab:** $v=b\sqrt[3]{\dfrac{A}{2B}}$.

@@ P54 | Latihan 54 | Sudut juring gelas kerucut | volume | 290
Gelas kerucut dibuat dari lingkaran berjari-jari $R$ dengan membuang juring $\theta$. $\theta$ berapa memberi volume maksimum?

{{fig:t_p54}}
===
Volume maksimum saat $r^2=\tfrac23R^2$ (dari $V=\tfrac\pi3r^2\sqrt{R^2-r^2}$), dan $2\pi r=(2\pi-\theta)R$.

**Jawab:** $\theta=2\pi\left(1-\sqrt{2/3}\right)\approx1{,}15$ rad $\approx66^\circ$.

@@ P55 | Latihan 55 | Jarak baca rambu jalan | struktur | 290
Huruf pada rambu setinggi 1 m dengan bagian bawah 5 m di atas jalan; mata pengemudi 1,5 m. Pada jarak berapa huruf tampak paling tinggi?

{{fig:t_p55}}
===
Tepi huruf $3{,}5$ m dan $4{,}5$ m di atas mata:

$$\theta=\arctan\frac{4{,}5}{x}-\arctan\frac{3{,}5}{x},\quad\theta'=0\Rightarrow x^2=3{,}5\times4{,}5.$$

**Jawab:** $x=\sqrt{15{,}75}\approx3{,}97$ m.

@@ P56 | Latihan 56 | Kecepatan optimum pesawat jet | gerak | 290
Gaya dorong $F=\tfrac12\rho Av^2\left(0{,}000182+\dfrac{4w^2}{6{,}5\pi\rho^2A^2v^4}\right)$ dengan $A=1600$, $w=150\,000$. Laju optimum meminimumkan $F/v$. (a) $\rho=0{,}0238$; (b) pada 30 000 kaki ($\rho$ dikali 0,375).
===
$F/v=\alpha v+\beta v^{-3}$, turunan nol saat

$$v^4=\frac{3\cdot4w^2}{6{,}5\pi\rho^2A^2(0{,}000182)}.$$

(a) $v\approx473$ mil/jam.

(b) $v\propto\rho^{-1/2}$, sehingga $v\approx473/\sqrt{0{,}375}\approx773$ mil/jam.

Catatan: nilai $\rho=0{,}0238$ mengikuti cetakan buku; kerapatan udara standar di permukaan laut adalah sekitar $0{,}00238$ slug/ft³, jadi kemungkinan ada salah cetak atau perbedaan satuan.

@@ P57 | Latihan 57 | Sudut gaya minimum melawan gesekan | gerak | 290
Gaya minimum untuk menggerakkan benda: $F=\dfrac{\mu mg}{\cos\theta+\mu\sin\theta}$. Cari $\theta$ yang meminimumkan $F$.

{{fig:t_p57}}
===
Maksimumkan penyebut: $-\sin\theta+\mu\cos\theta=0$.

**Jawab:** $\theta=\arctan\mu$.

@@ P58 | Latihan 58 | Jumlah jarak minimum, alas 2b | struktur | 290
Ulangi latihan 20 jika alas $2b$ sedangkan tinggi tetap $2a$.
===
$S=(2a-y)+2\sqrt{b^2+y^2}$, $S'=0\Rightarrow y=\dfrac{b}{\sqrt3}$.

**Jawab:** $y=b/\sqrt3$ bila $b\le2\sqrt3a$; jika lebih besar, $S$ turun pada seluruh $[0,2a]$ sehingga $P=A$ ($y=2a$).

@@ P59 | Latihan 59 | Laju truk berbiaya minimum | biaya | 290
Untuk $80\le v\le100$ km/jam, konsumsi truk $f(v)=a-bv$ km/L ($b>0$). Upah sopir $w$ per jam, harga bahan bakar $p$ per liter. Cari laju anjuran.
===
Biaya per km: $c(v)=\dfrac wv+\dfrac{p}{a-bv}$,

$$c'=-\frac{w}{v^2}+\frac{pb}{(a-bv)^2}=0\Rightarrow v^*=\frac{a\sqrt w}{b\sqrt w+\sqrt{pb}}.$$

**Jawab:** pakai $v^*$ jika di $[80,100]$; jika $v^*<80$ pakai $80$, jika $v^*>100$ pakai $100$.

@@ P60 | Latihan 60 | Rumus jarak titik ke garis | dasar | 290
Buktikan rumus jarak titik $(x_0,y_0)$ ke garis dengan meminimumkan fungsi jarak.
===
Garis $Ax+By+C=0$ ($B\ne0$): $y=-\dfrac{Ax+C}{B}$. Misalkan $f=(x-x_0)^2+(y-y_0)^2$. Dari $f'=0$:

$$(x-x_0)-\frac AB(y-y_0)=0,$$

sehingga $x-x_0=At$, $y-y_0=Bt$. Substitusi ke garis: $t=-\dfrac{Ax_0+By_0+C}{A^2+B^2}$. Maka

$$d=|t|\sqrt{A^2+B^2}=\frac{|Ax_0+By_0+C|}{\sqrt{A^2+B^2}}.$$

Kasus $B=0$ langsung: $d=|x_0+C/A|$. $\blacksquare$

@@ P61 | Latihan 61 | Jendela dengan batas biaya | biaya | 291
Jendela persegi panjang beratap setengah lingkaran: kaca bening $a$ per satuan luas, kaca berwarna $b$ (meneruskan fraksi $p$ cahaya), rangka lengkung $c$ per satuan panjang. Biaya tak melebihi $A$. Cari dimensi dengan cahaya terbanyak.

{{fig:t_win}}
===
Jari-jari $r$, tinggi $h$: $2arh+\tfrac12\pi br^2+\pi cr=A$. Substitusi $h$ ke cahaya $L=2rh+\tfrac12\pi pr^2$:

$$L(r)=\frac Aa-\frac{\pi c}{a}r-\frac{\pi(b-pa)}{2a}r^2,\qquad 0<r\le r_{\max}$$

($r_{\max}$ saat $h=0$). Turunan keduanya bertanda $pa-b$, dan $L'(r)=-\dfrac\pi a\,[c+(b-pa)r]$.

- Jika $b\ge pa$: $L$ selalu turun. Cahaya mendekati $A/a$ saat $r\to0$ (jendela makin sempit dan tinggi), tetapi tidak pernah tercapai.
- Jika $b<pa$: titik kritis $r=c/(pa-b)$ adalah **minimum**, sehingga maksimum ada di ujung: bandingkan $A/a$ (limit $r\to0$) dengan $L(r_{\max})=\tfrac12\pi pr_{\max}^2$.

**Kesimpulan:** sebagaimana dirumuskan, tidak ada optimum di dalam domain; diperlukan batas lebar minimum atau tinggi maksimum agar desainnya praktis.

@@ P62 | Latihan 62 | Titik elips terdekat | lintasan | 291
Cari titik pada $4x^2+9y^2=36$ yang terdekat dengan $\left(4,\dfrac{13\sqrt5}{6}\right)$.
===
$x=3\cos t$, $y=2\sin t$. Syarat turunan nol:

$$-10\sin t\cos t+24\sin t-\frac{26\sqrt5}{3}\cos t=0,$$

dipenuhi oleh $\cos t=\tfrac23$, $\sin t=\tfrac{\sqrt5}{3}$.

**Jawab:** $\left(2,\dfrac{2\sqrt5}{3}\right)$, jarak $\dfrac{\sqrt{61}}{2}$.

@@ P63 | Latihan 63 | Diagonal rangka layang-layang | struktur | 291
Rangka layang-layang dengan sisi luar $a,a,b,b$ ($b>a$). Berapa panjang diagonal agar luas maksimum?

{{fig:t_p63}}
===
Luas $=ab\sin\gamma$ dengan $\gamma$ sudut antara sisi $a$ dan $b$; maksimum di $\gamma=90^\circ$.

**Jawab:** diagonal sumbu $\sqrt{a^2+b^2}$, diagonal melintang $\dfrac{2ab}{\sqrt{a^2+b^2}}$.

@@ P64 | Latihan 64 | Segitiga terbesar di bawah tali busur parabola | geometri | 291
Garis $Ax+By+C=0$ memotong parabola $y=ax^2+bx+c$ di $P$ dan $Q$. Cari $R$ pada busur $PQ$ yang memaksimumkan luas segitiga $PQR$.

{{fig:t_p64}}
===
Alas $PQ$ tetap, jadi maksimumkan jarak $R$ ke garis, sebanding $|Ax+B(ax^2+bx+c)+C|$. Turunannya nol bila $A+B(2ax+b)=0$ (garis singgung sejajar $PQ$).

**Jawab:** $x_R=-\dfrac{b+A/B}{2a}$, $y_R=ax_R^2+bx_R+c$ (absisnya di tengah $x_P$ dan $x_Q$).

@@ P65 | Latihan 65 | Segitiga singgung terkecil pada kurva akar | geometri | 291
Garis singgung $y=\sqrt{1-x}$ membentuk segitiga dengan sumbu positif. Cari luas terkecil.
===
Titik singgung dengan $u=\sqrt{1-x}$: intersep $x=1+u^2$, $y=\dfrac{1+u^2}{2u}$.

$$A=\frac{(1+u^2)^2}{4u},\quad A'=0\Rightarrow3u^2=1.$$

**Jawab:** $\dfrac{4\sqrt3}{9}\approx0{,}770$.

@@ P66 | Latihan 66 | Panjang lengan irigasi pivot | biaya | 291
Lahan persegi $s\times s$: laba $a$/m² tanpa irigasi dan $b$/m² bila diairi; biaya irigasi $c$/m². Lengan berputar di pusat. Panjang lengan optimum? ($b>a+c$)

{{fig:t_p66}}
===
Keuntungan: $P=as^2+(b-a)A_{\text{dalam}}(r)-c\pi r^2$. Untuk $r\le s/2$, $P$ naik. Untuk $s/2<r<s/\sqrt2$, $\dfrac{dA_{\text{dalam}}}{dr}=r(2\pi-8\alpha)$ dengan $\cos\alpha=\dfrac{s}{2r}$. Maka

$$P'=r\,[(b-a)(2\pi-8\alpha)-2\pi c]=0\Rightarrow\alpha=\frac\pi4\left(1-\frac{c}{b-a}\right).$$

**Jawab:** $r=\dfrac s2\sec\left[\dfrac\pi4\left(1-\dfrac{c}{b-a}\right)\right]$ (diasumsikan air di luar lahan tetap berbiaya).

@@ P67 | Latihan 67 | Segiempat engsel terluas | struktur | 291
Batang 1 m, 4 m, 2 m, dan 3 m disambung engsel menjadi segiempat. Cari luas terbesar.

{{fig:t_p67}}
===
$K=\tfrac12(pq\sin\alpha+rs\sin\gamma)$ dengan kendala diagonal $p^2+q^2-2pq\cos\alpha=r^2+s^2-2rs\cos\gamma$. Turunan implisit memberi $\sin(\alpha+\gamma)=0$, yaitu $\alpha+\gamma=\pi$ (segiempat tali busur). Rumus Brahmagupta dengan setengah keliling 5:

$$K=\sqrt{(5-1)(5-4)(5-2)(5-3)}.$$

**Jawab:** $2\sqrt6\approx4{,}90\ \text{m}^2$.

@@ P68 | Latihan 68 | Rute tercepat mengitari danau | lintasan | 291
Danau lingkaran berjari-jari $r$ dikelilingi pantai sempit, di luarnya semak. $P$ dan $Q$ pada perpanjangan diameter, masing-masing $s$ dari pusat. Laju di pantai dua kali laju di semak. Rancang rute tercepat.

{{fig:t_p68a t_p68b}}
===
Rute: lurus dari $P$ ke pantai (sudut pusat $\varphi$), menyusuri pantai, lurus ke $Q$:

$$T(\varphi)\propto2\sqrt{s^2+r^2-2sr\cos\varphi}+\frac{r(\pi-2\varphi)}{2}.$$

$T'=0\Rightarrow2s\sin\varphi=\sqrt{s^2+r^2-2sr\cos\varphi}$.

**Jawab:** $\cos\varphi=\dfrac{r+\sqrt{12s^2-3r^2}}{4s}$; ruas semak membuat sudut $30^\circ$ dengan arah radial saat mencapai pantai.

@@ P69 | Latihan 69 | Persegi panjang luar terbesar | geometri | 291
Cari luas terbesar persegi panjang yang sisinya melalui keempat sudut persegi panjang $w\times L$.
===
$A(\theta)=(L\cos\theta+w\sin\theta)(L\sin\theta+w\cos\theta)=Lw+\dfrac{L^2+w^2}{2}\sin2\theta$.

**Jawab:** $\dfrac{(L+w)^2}{2}$.

@@ P70 | Latihan 70 | Posisi patok dengan total tali minimum | lintasan | 291
Ada $n$ patok merah pada satu garis. Di mana patok biru dipasang agar total panjang tali ke semua patok minimum?
===
Dengan posisi $a_1\le\dots\le a_n$: $S(x)=\sum|x-a_i|$. Di antara patok, $S'(x)=$ (jumlah patok di kiri) $-$ (jumlah di kanan). $S$ turun selama patok kiri lebih sedikit, lalu naik.

**Jawab:** di **median**: pada patok tengah jika $n$ ganjil; di mana saja antara dua patok tengah jika $n$ genap.

@@ P71 | Latihan 71 | Sudut percabangan pipa dengan hambatan minimum | air | 291–292
Hambatan aliran laminar (Poiseuille) $R=kL/r^4$. Cabang berjari-jari $r_2<r_1$ keluar dari pipa utama di $D$ menuju $C$. (a) Nyatakan $R(\theta)$. (b)–(c) Cari titik kritis dan jenisnya. (d) Tunjukkan nilainya. (e) Apakah minimum mutlak?

{{fig:t_p71}}
===
(a) $L_2=Y\csc\theta$ dan $L_1=X-Y\cot\theta$:

$$R=\frac{k}{r_1^4}(X-Y\cot\theta)+\frac{k}{r_2^4}Y\csc\theta.$$

(b) $R'=kY\csc^2\theta\left(\dfrac1{r_1^4}-\dfrac{\cos\theta}{r_2^4}\right)=0\Rightarrow\cos\bar\theta=\dfrac{r_2^4}{r_1^4}$.

(c) $R'$ berubah dari negatif ke positif: minimum relatif.

(d) $R(\bar\theta)=\dfrac{kX}{r_1^4}+\dfrac{kY}{r_2^4}\sqrt{1-(r_2/r_1)^8}$, lebih kecil dari $R(\pi/2)=\dfrac{kX}{r_1^4}+\dfrac{kY}{r_2^4}$.

(e) Satu-satunya titik kritis pada $(0,\pi/2)$, jadi minimum mutlak di sana, asalkan $D$ tetap berada di antara $A$ dan $E$, yaitu $X\ge Y\cot\bar\theta$.

@@ P72 | Latihan 72 | Silinder berluas permukaan maksimum dalam kerucut | volume | 292
Kerucut berjari-jari $R$ dan tinggi $H$. Cari jari-jari silinder di dalamnya agar luas total (tutup, alas, selimut) maksimum.

{{fig:t_p72}}
===
$$S(x)=2\pi x^2+2\pi xH\left(1-\frac xR\right),\qquad0\le x\le R.$$

$S'=0\Rightarrow x=\dfrac{HR}{2(H-R)}$.

**Jawab:** jika $H>2R$, $x=\dfrac{HR}{2(H-R)}$. Jika $H\le2R$, $S$ naik terus dan maksimum di $x=R$ (silinder pipih, $S=2\pi R^2$).

@@ P74 | Latihan 74 | Sudut tali pada sistem tiga cincin | struktur | 292
Tali bercincin di satu ujung dilewatkan pada dua cincin tetap sejajar, lalu ujung lainnya melalui cincin tadi dan diberi massa $m$. Sistem bergerak hingga $m$ sejauh mungkin di bawah garis cincin tetap. Cari $\theta$.

{{fig:t_p74}}
===
Jarak cincin tetap $D$, panjang tali $L$, $\varphi=\theta/2$. Kedalaman massa:

$$y=\frac D2\cot\varphi+\left(L-D-D\csc\varphi\right).$$

$y'=D\csc^2\varphi\left(\cos\varphi-\tfrac12\right)=0\Rightarrow\varphi=\dfrac\pi3$.

**Jawab:** $\theta=120^\circ$.

@@ P75 | Latihan 75 | Pagar berbentuk busur lingkaran | struktur | 292
Jika 1000 m pagar pada Contoh 4.22 dibentuk busur lingkaran (sungai sebagai tali busur), berapa luas maksimumnya?

{{fig:t_p75}}
===
Sudut pusat $\alpha$, $R=1000/\alpha$:

$$A=\frac{1000^2(\alpha-\sin\alpha)}{2\alpha^2},\quad A'\propto2\sin\alpha-\alpha(1+\cos\alpha)=0\Rightarrow\alpha=\pi.$$

**Jawab:** setengah lingkaran, $A=\dfrac{1000^2}{2\pi}\approx159\,155\ \text{m}^2$.

@@ P76 | Latihan 76 | Lipatan kertas terpendek | geometri | 292
Sudut kiri atas kertas selebar $a$ dan sepanjang $b>a$ dilipat ke tepi kanan. Cari $x$ agar panjang lipatan $y$ minimum.

{{fig:t_p76}}
===
Bayangan sudut berada $d=\sqrt{2ax-a^2}$ di bawah tepi atas; titik lipat di tepi kiri berjarak $z=ax/d$. Maka

$$y^2=x^2+z^2=\frac{2x^3}{2x-a},\qquad\frac a2<x\le a.$$

Turunan $\propto x^2(4x-3a)=0$.

**Jawab:** $x=\tfrac34a$, $y=\dfrac{3\sqrt3}{4}a$ (berlaku jika $b\ge\dfrac{3a}{2\sqrt2}$).

@@ P77 | Latihan 77 | Segitiga terbesar pada tali busur elips | geometri | 292
Garis $y=mx+c$ memotong elips $b^2x^2+a^2y^2=a^2b^2$ di $P,Q$. Cari $R$ pada elips agar luas $PQR$ maksimum.
===
Maksimumkan jarak ke garis: di titik singgung yang sejajar garis, yaitu $-\dfrac{b^2x}{a^2y}=m$.

**Jawab:** untuk $c>0$, $R=\left(\dfrac{a^2m}{\sqrt{a^2m^2+b^2}},\ \dfrac{-b^2}{\sqrt{a^2m^2+b^2}}\right)$; untuk $c<0$ ambil titik berlawanan (untuk $c=0$ keduanya setara).

@@ P78 | Latihan 78 | Talang berpenampang busur | air | 293
Lembaran selebar $a$ dan panjang $L$ dibentuk talang berpenampang busur lingkaran dengan tutup ujung. Cari jari-jari agar volume maksimum.

{{fig:t_p78}}
===
$r=a/\alpha$ dan luas tembereng $\dfrac{r^2}{2}(\alpha-\sin\alpha)=\dfrac{a^2(\alpha-\sin\alpha)}{2\alpha^2}$. Seperti latihan 75, maksimum di $\alpha=\pi$.

**Jawab:** $r=\dfrac a\pi$ (setengah lingkaran), $V=\dfrac{a^2L}{2\pi}$.
