@@ C29 | Contoh 4.29 | Membaca gerak dari fungsi posisi | gerak | 294–295
Partikel pada sumbu-$x$: $x(t)=3t^4-32t^3+114t^2-144t+40$, $0\le t\le5$ (m, s). (a) Kecepatan dan laju di $t=\tfrac12$? (b) Kapan percepatan naik? (c) Di $t=2$ kecepatan naik atau turun? (d) Di $t=2$ makin cepat atau melambat? (e) Kecepatan maksimum pada $[0; 2]$? (f) Jarak terjauh dari titik asal?

{{fig:t_c29}}
===
$$v=12(t-1)(t-3)(t-4),\qquad a=12(3t^2-16t+19).$$

- (a) $v(\tfrac12)=-\tfrac{105}{2}$ m/s; laju $\tfrac{105}{2}$ m/s.
- (b) $\dfrac{da}{dt}=24(3t-8)\ge0$ untuk $\tfrac83\le t\le5$.
- (c) $a(2)=-12<0$: kecepatan turun.
- (d) $v(2)=24>0$ berlawanan tanda dengan $a(2)$: melambat.
- (e) $a=0$ di $t=\dfrac{8-\sqrt7}{3}$; $v_{\max}\approx25{,}35$ m/s.
- (f) Terjauh di $t=5$: $45$ m.

{{fig:t_c29v}}

@@ C30 | Contoh 4.30 | Massa pada pegas yang dipukul | gerak | 296–297
Massa $M$ pada pegas ($k$) disimpangkan $x_0$ lalu dilepas, dan pada $t=t_0$ dipukul gaya impuls $F$: $Mx''+kx=F\thinspace \delta(t-t_0)$, $x(0)=x_0$, $x'(0)=0$. (a) Verifikasi solusi. (b) Tunjukkan kecepatan berubah sebesar $F/M$.

$$x(t)=x_0\cos\omega t+\frac{F}{\sqrt{kM}}\sin\omega(t-t_0)\thinspace h(t-t_0),\qquad\omega=\sqrt{k/M}.$$

{{fig:t_c30}}
===
(a) Untuk $t\ne t_0$ turunan fungsi tangga $h$ nol:

$$x'=-\omega x_0\sin\omega t+\frac FM\cos\omega(t-t_0)\thinspace h,$$

$$x''=-\omega^2x_0\cos\omega t-\frac{F\omega}{M}\sin\omega(t-t_0)\thinspace h.$$

Jadi $Mx''+kx=0$ untuk $t\ne t_0$, serta $x(0)=x_0$ dan $x'(0)=0$.

(b) $x'(t_0^+)-x'(t_0^-)=\dfrac FM\cos0=\dfrac FM$. $\blacksquare$

Ini model dasar **beban impuls pada struktur** (dinamika struktur satu derajat kebebasan).

@@ C31 | Contoh 4.31 | Kecepatan dan percepatan peluncur engkol | gerak | 297–298
Batang $AB$ berputar berlawanan jarum jam dengan kecepatan sudut tetap $\omega$; ujung $C$ batang $BC$ meluncur pada garis horizontal (offset $e$). Tentukan kecepatan dan percepatan $C$.

{{fig:t_c31}}
===
$$x=r\cos\theta+L\cos\phi,\qquad e=L\sin\phi-r\sin\theta.$$

Turunkan persamaan offset: $\dot\phi=\dfrac{\omega r\cos\theta}{L\cos\phi}$. Substitusi ke $\dot x$:

$$v=-\frac{\omega r\sin(\theta+\phi)}{\cos\phi}.$$

Turunkan sekali lagi:

$$a=-\frac{\omega^2r}{L\cos^3\phi}\left[L\cos^2\phi\cos(\theta+\phi)+r\cos^2\theta\right].$$

@@ P1 | Latihan 1 | Gerak linear | gerak | 298
Bahas gerak $x(t)=2t+5$, $t\ge5$.
===
$v=2$, $a=0$. Mulai di $x=15$ m dan bergerak ke kanan dengan laju tetap.

@@ P2 | Latihan 2 | Gerak kuadratik | gerak | 298
Bahas gerak $x(t)=t^2-7t+6$, $t\ge0$.
===
$v=2t-7$, $a=2$. Mulai di $x=6$ ke kiri sambil melambat, berhenti di $t=3{,}5$ ($x=-6{,}25$), lalu ke kanan makin cepat. Melewati titik asal pada $t=1$ dan $t=6$.

@@ P3 | Latihan 3 | Gerak kuadratik searah | gerak | 298
Bahas gerak $x(t)=t^2+5t+10$, $t\ge1$.
===
$v=2t+5>0$, $a=2>0$. Mulai di $x=16$, terus ke kanan dan makin cepat.

@@ P4 | Latihan 4 | Gerak kubik | gerak | 298
Bahas gerak $x(t)=-2t^3+2t^2+16t-1$, $t\ge0$.
===
$v=-2(3t+4)(t-2)$, $a=4-12t$. Mulai di $x=-1$ ke kanan ($v=16$); makin cepat sampai $t=\tfrac13$, melambat dan berhenti di $t=2$ ($x=23$), lalu ke kiri makin cepat.

@@ P5 | Latihan 5 | Gerak kubik dua kali berbalik | gerak | 298
Bahas gerak $x(t)=t^3-9t^2+15t+3$, $t\ge2$.
===
$v=3(t-1)(t-5)$, $a=6t-18$. Di $t=2$: $x=5$, $v=-9$. Ke kiri makin cepat sampai $t=3$ ($x=-6$), melambat dan berhenti di $t=5$ ($x=-22$), lalu ke kanan makin cepat.

@@ P6 | Latihan 6 | Gerak harmonik sederhana | gerak | 298
Bahas gerak $x(t)=3\cos4t$, $t\ge0$.
===
$v=-12\sin4t$, $a=-48\cos4t=-16x$. Osilasi dengan amplitudo $3$ m dan periode $\pi/2$ s. Laju maksimum $12$ m/s di $x=0$; besar percepatan maksimum $48$ m/s² di $x=\pm3$ m (percepatan bertanda $a$ maksimum, $+48$ m/s², hanya di $x=-3$ m).

@@ P7 | Latihan 7 | Gerak hiperbolik | gerak | 298
Bahas gerak $x(t)=1/t$, $t\ge1$.
===
$v=-1/t^2<0$, $a=2/t^3>0$. Dari $x=1$ bergerak ke kiri, melambat, mendekati titik asal tanpa pernah mencapainya.

@@ P8 | Latihan 8 | Gerak dengan satu titik balik | gerak | 298
Bahas gerak $x(t)=t+4/t$, $t\ge1$.
===
$v=1-4/t^2$, $a=8/t^3>0$. Dari $x=5$ ke kiri sambil melambat, berbalik di $t=2$ ($x=4$), lalu ke kanan; laju mendekati $1$ m/s.

@@ P9 | Latihan 9 | Gerak rasional | gerak | 298
Bahas gerak $x(t)=(t-4)/t^2$, $t\ge2$.
===
$$v=\frac{8-t}{t^3},\qquad a=\frac{2(t-12)}{t^4}.$$

Mulai $x=-\tfrac12$ ke kanan, melewati titik asal di $t=4$, berbalik di $t=8$ ($x=\tfrac1{16}$), lalu kembali mendekati $0$. Makin cepat pada $8<t<12$, melambat pada $2<t<8$ dan $t>12$.

@@ P10 | Latihan 10 | Gerak dengan akar | gerak | 298
Bahas gerak $x(t)=(t-1)^2\sqrt t$, $t\ge1$.
===
$$v=\frac{(t-1)(5t-1)}{2\sqrt t},\qquad a=\frac{15t^2-6t-1}{4t^{3/2}}>0.$$

Mulai diam di titik asal, lalu bergerak ke kanan makin cepat.

@@ P11 | Latihan 11 | Analisis lengkap gerak kubik | gerak | 298
$x(t)=t^3-9t^2+24t+1$, $0\le t\le6$. Tentukan (a) laju naik atau turun di $t=1$; (b) kecepatan maksimum/minimum; (c) laju maksimum/minimum; (d) percepatan maksimum/minimum; (e) kapan percepatan naik.
===
$v=3(t-2)(t-4)$, $a=6t-18$.

- (a) $v(1)=9>0$, $a(1)=-12<0$: laju **turun**.
- (b) $v_{\max}=24$ (pada $t=0$ s dan $t=6$ s), $v_{\min}=-3$ (di $t=3$).
- (c) Laju maksimum $24$, minimum $0$ (pada $t=2$ s dan $t=4$ s).
- (d) $a_{\max}=18$ ($t=6$), $a_{\min}=-18$ ($t=0$).
- (e) $da/dt=6>0$: selalu naik.

@@ P12 | Latihan 12 | Analisis gerak kubik kedua | gerak | 298
Ulangi latihan 11 untuk $x(t)=2-15t+9t^2-t^3$, $0\le t\le6$.
===
$v=-3(t-1)(t-5)$, $a=18-6t$.

- (a) Di $t=1$ laju bernilai $0$ (minimum): turun sebelum $t=1$ dan naik sesudahnya.
- (b) $v_{\max}=12$ ($t=3$), $v_{\min}=-15$ (pada $t=0$ s dan $t=6$ s).
- (c) Laju maksimum $15$, minimum $0$ (pada $t=1$ s dan $t=5$ s).
- (d) $a_{\max}=18$ ($t=0$), $a_{\min}=-18$ ($t=6$).
- (e) $da/dt=-6<0$: tidak pernah naik.

@@ P13 | Latihan 13 | Akar kecepatan dengan metode Newton | gerak | 298
$x(t)=t\sin t$, $0\le t\le9$. (a) Gambarkan grafiknya. (b) Kapan kecepatan nol? (c) Kapan percepatan sama dengan 1?
===
(a) Lihat grafik di bawah.

(b) $v=\sin t+t\cos t=0$. Newton: $t_{n+1}=t_n-\dfrac{v(t_n)}{v'(t_n)}$ memberi $t=0$, $2{,}029$, $4{,}913$, $7{,}979$ s.

(c) $a=2\cos t-t\sin t=1$ memberi $t\approx0{,}731$, $3{,}853$, $6{,}436$ s.

@@ P14 | Latihan 14 | Interval kecepatan dan laju | gerak | 298
$x(t)=3t^4-16t^3+18t^2+2$, $0\le t\le4$. Tentukan interval naik/turun kecepatan dan laju, ekstrem kecepatan dan laju, jarak terjauh dari titik asal, dan dari $x=5$.
===
$v=12t(t-1)(t-3)$, $a=12(3t^2-8t+3)$; $a=0$ pada $t_{1,2}=\dfrac{4\mp\sqrt7}{3}$, yaitu $t_1\approx0{,}451$ s dan $t_2\approx2{,}215$ s.

- (a) $v$ naik pada $[0; t_1]$ dan $[t_2; 4]$; turun pada $[t_1; t_2]$.
- (b) Laju naik pada $(0; t_1)$, $(1; t_2)$, $(3; 4)$; turun pada $(t_1; 1)$, $(t_2; 3)$.
- (c) $v_{\max}=144$ ($t=4$), $v_{\min}\approx-25{,}35$ ($t=t_2$).
- (d) Laju maksimum $144$, minimum $0$ (pada $t=0$ s, $1$ s, dan $3$ s).
- (e) Jarak terjauh dari titik asal $34$ m ($t=4$).
- (f) Jarak terjauh dari $x=5$: $30$ m ($t=3$, $x=-25$).

@@ P15 | Latihan 15 | Interval gerak dengan koefisien pecahan | gerak | 298
Ulangi latihan 14 untuk $x(t)=\dfrac{14t^3}{45}-\dfrac{101t^2}{45}+\dfrac{132t}{45}+2$, $0\le t\le6$.
===
$v=\dfrac{42t^2-202t+132}{45}$ nol pada $t\approx0{,}780$ s dan $t\approx4{,}030$ s; $a=\dfrac{84t-202}{45}$ nol di $t=\dfrac{101}{42}\approx2{,}405$.

- (a) $v$ turun pada $[0; 2{,}405]$, naik pada $[2{,}405; 6]$.
- (b) Laju naik pada $(0{,}780; 2{,}405)$ dan $(4{,}030; 6)$; turun pada $(0; 0{,}780)$ dan $(2{,}405; 4{,}030)$.
- (c) $v_{\max}=9{,}6$ ($t=6$), $v_{\min}\approx-2{,}46$.
- (d) Laju maksimum $9{,}6$, minimum $0$.
- (e) Jarak terjauh dari titik asal $6$ m ($t=6$).
- (f) Jarak terjauh dari $x=5$: $\approx7{,}27$ m ($t\approx4{,}030$).

@@ P16 | Latihan 16 | Kecepatan dan percepatan nol bersamaan | gerak | 298
Ciri apa pada grafik posisi yang menandai saat kecepatan dan percepatan sama-sama nol?

{{fig:t_flat}}
===
Garis singgung **datar** ($x'=0$) sekaligus kelengkungan nol ($x''=0$). Umumnya berupa **titik belok horizontal**; bisa juga bagian yang sangat rata, misalnya ekstrem pada $x=(t-c)^4$, atau selang saat partikel diam.

@@ P17 | Latihan 17 | Titik kritis kecepatan dan laju | gerak | 299
Apakah titik kritis fungsi kecepatan sama dengan titik kritis fungsi laju? Jelaskan dengan grafik.

{{fig:t_speed}}
===
Tidak selalu. Laju $|v|$ memiliki semua titik kritis $v$ (dengan $v\ne0$), ditambah titik **sudut** di tempat $v$ berganti tanda ($v=0$, $a\ne0$). Di sana $|v|$ minimum walaupun $v$ tidak punya titik kritis.

@@ P18 | Latihan 18 | Laju maksimum pada Contoh 4.29 | gerak | 299
Berapa laju maksimum partikel Contoh 4.29 pada $0\le t\le2$?
===
$v$ naik dari $v(0)=-144$ ke maksimum $\approx25{,}35$ lalu $v(2)=24$.

**Jawab:** $144$ m/s di $t=0$.

@@ P19 | Latihan 19 | Percepatan sebagai fungsi posisi | gerak | 299
Tunjukkan percepatan dapat ditulis $a=v\thinspace \dfrac{dv}{dx}$.
===
Aturan rantai: $a=\dfrac{dv}{dt}=\dfrac{dv}{dx}\cdot\dfrac{dx}{dt}=v\dfrac{dv}{dx}$. $\blacksquare$

@@ P20 | Latihan 20 | Maksimum posisi dan jarak | gerak | 299
Benar atau salah: jika posisi memiliki maksimum relatif, jarak ke titik asal $|x|$ juga.
===
**Tidak selalu.** Benar jika $x(t_0)>0$. Jika $x(t_0)<0$, $|x|=-x$ justru minimum relatif; jika $x(t_0)=0$ maksimum, $|x|$ juga minimum.

@@ P21 | Latihan 21 | Minimum posisi dan jarak | gerak | 299
Benar atau salah: jika posisi memiliki minimum relatif, $|x|$ juga.
===
**Tidak selalu.** Benar jika $x(t_0)\ge0$. Jika $x(t_0)<0$, $|x|$ memiliki maksimum relatif.

@@ P22 | Latihan 22 | Minimum kecepatan dan laju | gerak | 299
Benar atau salah: jika kecepatan minimum relatif, laju juga.
===
**Tidak selalu.** Benar jika $v(t_0)\ge0$. Jika $v(t_0)<0$, laju $=-v$ maksimum relatif.

@@ P23 | Latihan 23 | Maksimum kecepatan dan laju | gerak | 299
Benar atau salah: jika kecepatan maksimum relatif, laju juga.
===
**Tidak selalu.** Benar jika $v(t_0)>0$. Jika $v(t_0)\le0$, laju memiliki minimum relatif.

@@ P24 | Latihan 24 | Posisi peluncur sebagai fungsi sudut | gerak | 299
(a) Tunjukkan $x=r\cos\theta+\sqrt{L^2-(e+r\sin\theta)^2}$. (b) Gambarkan grafiknya untuk $L=9$, $r=2$, $e=1$ cm. (c) Perkirakan langkah. (d) Turunkan kecepatan. (e) Gambarkan grafik kecepatan untuk 1 putaran per detik.

{{fig:t_c31}}
===
(a) $\sin\phi=\dfrac{e+r\sin\theta}{L}$, jadi $L\cos\phi=\sqrt{L^2-(e+r\sin\theta)^2}$; masukkan ke $x=r\cos\theta+L\cos\phi$.

(b)

{{fig:t_p24x}}

(c) Langkah $=\sqrt{11^2-1}-\sqrt{7^2-1}=\sqrt{120}-\sqrt{48}\approx4{,}03$ cm, sesuai selisih titik tertinggi dan terendah grafik.

(d) $v=\dfrac{dx}{d\theta}\thinspace \omega=-\omega r\left[\sin\theta+\dfrac{\cos\theta\thinspace (e+r\sin\theta)}{\sqrt{L^2-(e+r\sin\theta)^2}}\right]=-\dfrac{\omega r\sin(\theta+\phi)}{\cos\phi}$.

(e) Dengan $\omega=2\pi$:

{{fig:t_p24v}}

Kecepatan nol tepat di titik tertinggi dan terendah grafik posisi. Dari grafik, $v_{\max}\approx12{,}6$ cm/s dan $v_{\min}\approx-13{,}3$ cm/s.

@@ P25 | Latihan 25 | Kapan mulai turun pada pendaratan | struktur | 299
Lintasan pendaratan: tinggi $h$ saat mulai turun, mendarat mulus di $x=0$, laju horizontal tetap $U$, besar percepatan vertikal tidak melebihi $k$, lintasan polinomial kubik. Kapan penurunan harus dimulai?

{{fig:t_p25b}}
===
Syarat $y(0)=y'(0)=0$, $y(D)=h$, $y'(D)=0$:

$$y=h\left(\frac{3x^2}{D^2}-\frac{2x^3}{D^3}\right).$$

Karena $x$ berubah dengan laju $U$:

$$\ddot y=U^2y''=U^2h\left(\frac{6}{D^2}-\frac{12x}{D^3}\right),\quad\max|\ddot y|=\frac{6hU^2}{D^2}\le k.$$

**Jawab:** mulai turun pada jarak horizontal $D\ge U\sqrt{\dfrac{6h}{k}}$.
