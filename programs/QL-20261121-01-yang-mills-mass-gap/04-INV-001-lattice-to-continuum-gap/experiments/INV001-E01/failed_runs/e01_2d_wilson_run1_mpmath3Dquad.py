#!/usr/bin/env python3
# Witness Labs, Agentic Swarm, 0ait | © 2026 Witness Labs, Agentic Swarm, 0ait. All rights reserved. | contributing agent: QUASAR | x-witness-labs-attribution
"""INV001-E01: 2D Wilson lattice gauge theory, SU(2) and U(1), exact character expansion.

Conventions (lattice units a=1):
  SU(2): plaquette weight w(U) = exp((beta/2) Re Tr U) = exp(beta cos th), U ~ diag(e^{i th}, e^{-i th}).
         Haar class measure (2/pi) sin^2 th dth on [0,pi]; chi_j(th) = sin((2j+1)th)/sin th.
         chat_j = int w chi_j dU = I_{2j}(beta) - I_{2j+2}(beta) = (2(2j+1)/beta) I_{2j+1}(beta)
         a_j = chat_j / d_j = 2 I_{2j+1}(beta)/beta,   t_j = a_j/a_0 = I_{2j+1}/I_1.
  U(1):  w = exp(beta cos th), a_n = I_n(beta), t_n = I_n/I_0.
Exact facts used (derived in INV001-D06 sec. E01 notes / RUN.md):
  * closed genus-1 surface (torus) with n plaquettes: Z = sum_r a_r^n  (Euler char 0).
  * transfer matrix on a spatial circle of L links (gauge-invariant sector = class functions of the
    spatial Polyakov loop P): eigenvectors chi_r(P), eigenvalues lambda_r = a_r^L.
  * full-sector lattice gap m_lat(beta,L) = -log(lambda_{1/2}/lambda_0) = L * sigma_lat(beta),
    sigma_lat = -log t_{1/2}; infinite-plane Wilson loop <W_C> = t_{1/2}^{Area}.
Cross-checks: (i) chat_j by direct quadrature vs Bessel closed form;
              (ii) Z on the 1x1 torus by direct 3-dimensional quadrature over SU(2)xSU(2) vs sum_j a_j.
"""
import mpmath as mp, json, sys, time
mp.mp.dps = 50
out = {}

def tj_su2(beta, j2):  # j2 = 2j
    return mp.besseli(j2+1, beta)/mp.besseli(1, beta)
def aj_su2(beta, j2):
    return 2*mp.besseli(j2+1, beta)/beta
def sigma_su2(beta):
    return -mp.log(tj_su2(beta, 1))
def sigma_u1(beta):
    return -mp.log(mp.besseli(1, beta)/mp.besseli(0, beta))

# ---- (i) quadrature cross-check of character coefficients
chk = []
for beta in [mp.mpf('0.5'), mp.mpf(2), mp.mpf(8), mp.mpf(30)]:
    for j2 in range(0, 5):
        f = lambda th: mp.exp(beta*mp.cos(th))*mp.sin((j2+1)*th)*mp.sin(th)*2/mp.pi
        q = mp.quad(f, [0, mp.pi/2, mp.pi])
        closed = mp.besseli(j2, beta) - mp.besseli(j2+2, beta)
        closed2 = 2*(j2+1)/beta*mp.besseli(j2+1, beta)
        chk.append(dict(beta=str(beta), j=j2/2, quad=mp.nstr(q, 30), closed=mp.nstr(closed, 30),
                        relerr=mp.nstr(abs(q-closed)/abs(closed), 5), recurrence_relerr=mp.nstr(abs(closed2-closed)/abs(closed), 5)))
out['coefficient_crosscheck'] = chk
print('max relerr quad vs Bessel:', max(float(c['relerr']) for c in chk))

# ---- (ii) 1x1 torus: Z = int int w(U V U^-1 V^-1) dU dV vs sum_j a_j
# V = diag(e^{i phi}, e^{-i phi}) weight (2/pi) sin^2 phi; U = cos al + i sin al (n.sigma),
# n = (sin vt cos ps, sin vt sin ps, cos vt), Haar: (2/pi) sin^2 al dal * (1/(4 pi)) sin vt dvt dps.
# Tr(U V U^-1 V^-1) depends only on al, vt, phi: computed in closed form below.
#   U V U^-1 V^-1 trace = 2[ cos^2 al + sin^2 al (cos^2 vt + sin^2 vt cos 2phi) ]  (derived; also checked numerically)
import numpy as np
def comm_trace_numeric(al, vt, ps, phi):
    sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]]); sz=np.array([[1,0],[0,-1]],complex)
    n=(np.sin(vt)*np.cos(ps), np.sin(vt)*np.sin(ps), np.cos(vt))
    U=np.cos(al)*np.eye(2)+1j*np.sin(al)*(n[0]*sx+n[1]*sy+n[2]*sz)
    V=np.diag([np.exp(1j*phi), np.exp(-1j*phi)])
    return np.trace(U@V@np.linalg.inv(U)@np.linalg.inv(V)).real
def comm_trace_closed(al, vt, phi):
    return 2*(np.cos(al)**2 + np.sin(al)**2*(np.cos(vt)**2 + np.sin(vt)**2*np.cos(2*phi)))
rng=np.random.default_rng(1)
mx=0
for _ in range(2000):
    al,vt,ps,phi=rng.uniform(0,np.pi),rng.uniform(0,np.pi),rng.uniform(0,2*np.pi),rng.uniform(0,np.pi)
    mx=max(mx,abs(comm_trace_numeric(al,vt,ps,phi)-comm_trace_closed(al,vt,phi)))
out['commutator_trace_formula_maxerr_2000_random'] = mx
print('commutator trace closed form max err:', mx)

tor = []
mp.mp.dps = 30
for beta in [mp.mpf('0.5'), mp.mpf(1), mp.mpf(3)]:
    def integrand(al, vt, phi):
        tr = 2*(mp.cos(al)**2 + mp.sin(al)**2*(mp.cos(vt)**2 + mp.sin(vt)**2*mp.cos(2*phi)))
        return mp.exp(beta*tr/2) * (2/mp.pi)*mp.sin(al)**2 * (mp.sin(vt)/2) * (2/mp.pi)*mp.sin(phi)**2
    t0=time.time()
    mp.mp.dps = 20
    Zq = mp.quad(integrand, [0, mp.pi/2, mp.pi], [0, mp.pi/2, mp.pi], [0, mp.pi/2, mp.pi])
    mp.mp.dps = 30
    Zc = mp.nsum(lambda j2: aj_su2(beta, int(j2)), [0, mp.inf])
    tor.append(dict(beta=str(beta), Z_quadrature=mp.nstr(Zq, 18), Z_character=mp.nstr(Zc, 18),
                    relerr=mp.nstr(abs(Zq-Zc)/Zc, 5), seconds=round(time.time()-t0,1)))
    print(tor[-1])
out['torus_1x1_crosscheck'] = tor
mp.mp.dps = 50

# ---- main tables: sigma_lat(beta), asymptotics, gap at fixed physical length
tab = []
for b in ['0.25','0.5','1','2','4','8','16','32','64','128','256','1024','4096']:
    beta = mp.mpf(b)
    s2 = sigma_su2(beta); s1 = sigma_u1(beta)
    tab.append(dict(beta=b, sigma_lat_SU2=mp.nstr(s2, 25), beta_times_sigma_SU2=mp.nstr(beta*s2, 20),
                    sigma_lat_U1=mp.nstr(s1, 25), beta_times_sigma_U1=mp.nstr(beta*s1, 20),
                    t_half_SU2=mp.nstr(tj_su2(beta,1),25), t_one_SU2=mp.nstr(tj_su2(beta,2),25)))
out['sigma_table'] = tab
# 2D continuum limit: fix sigma_phys = 1 (units), a(beta) = sqrt(sigma_lat(beta)); fix physical circle length ell
traj = []
for ell in [mp.mpf(1), mp.mpf(4)]:
    for b in ['4','16','64','256','1024','4096','16384']:
        beta = mp.mpf(b)
        a = mp.sqrt(sigma_su2(beta))          # lattice spacing in units sigma_phys^{-1/2}
        L = int(mp.nint(ell/a))               # number of spatial links
        m_lat = L*sigma_su2(beta)              # exact full-sector gap in lattice units on circle of L links
        traj.append(dict(ell=str(ell), beta=b, a=mp.nstr(a,15), L=L, ell_actual=mp.nstr(L*a,12),
                         m_lat=mp.nstr(m_lat,15), Delta_phys=mp.nstr(m_lat/a,15),
                         Delta_over_sigma_ell_actual=mp.nstr(m_lat/a/(L*a),15),
                         beta_a2=mp.nstr(beta*a*a,15)))
out['continuum_trajectory_SU2'] = traj
# Exact 2D decimation (Migdal, exact in 2D): blocking b x b plaquettes: t_r -> t_r^(b^2)
dec = []
beta = mp.mpf(64)
t = {j2: tj_su2(beta, j2) for j2 in range(0,4)}
for k in range(0,8):
    bb = 2**k
    dec.append(dict(block=bb, t_half=mp.nstr(t[1]**(bb*bb),15), t_one=mp.nstr(t[2]**(bb*bb),15),
                    t_threehalf=mp.nstr(t[3]**(bb*bb),15),
                    heat_kernel_check_t1_over_thalf_power=mp.nstr(mp.log(t[2]**(bb*bb))/mp.log(t[1]**(bb*bb)),12)))
out['exact_2D_decimation_from_beta64'] = dec
json.dump(out, open('outputs/e01_results.json','w'), indent=1)
print(json.dumps(tab[:3], indent=1)); print(json.dumps(traj, indent=1)); print(json.dumps(dec, indent=1))
