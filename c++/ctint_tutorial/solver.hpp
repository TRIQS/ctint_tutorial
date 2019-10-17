#include <triqs/gfs.hpp>

// ------------ The main class of the solver -----------------------

namespace ctint_tutorial {

  enum spin { up, down };

  using namespace triqs::gfs; 

  class solver {

    double beta;
    triqs::gfs::block_gf<imfreq> g0_iw, g0tilde_iw, g_iw, M_iw;
    triqs::gfs::block_gf<imtime> g0tilde_tau;

    public:
    /// Access non-interacting Matsubara Green function
    block_gf_view<imfreq> G0_iw() { return g0_iw; }

    /// Access non-interacting imaginary-time Green function
    block_gf_view<imtime> G0_tau() { return g0tilde_tau; }

    /// Access interacting Matsubara Green function
    block_gf_view<imfreq> G_iw() { return g_iw; }

    /// Construct a ctint solver
    solver(double beta_, int n_iw = 1024, int n_tau = 100001);

    /// Method that performs the QMC calculation
    void solve(double U, double delta, int n_cycles, int length_cycle = 50, int n_warmup_cycles = 5000, std::string random_name = "",
               int max_time = -1);
  };
} // namespace ctint_tutorial
