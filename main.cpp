#include <iostream>
#include <vector>
#include <cmath>
#include <numeric>

#include <boost/math/distributions/poisson.hpp>

double S_0, C = -0.01, L = 1;

double marginal_profit(int x) {
    boost::math::poisson_distribution<> dist(L);
    double t = boost::math::cdf(dist, x);
    return S_0 * t; // TODO
}

double gank_pdf(std::vector<double> sec_levels, double K, double E = 0.0) {
    double mu_s = std::accumulate(sec_levels.begin(), sec_levels.end(), 0) / sec_levels.size();
    double w1 = 1, w2 = 1, w3 = 0, w4 = 0; // TODO
    return w1*mu_s + w2*C + w3*E + w4*std::log(K/1e7); // TODO
}



int main(void) {
    // Value of the trade initially.
    double margin, volume, ppu;
    std::cin >> margin >> volume >> ppu;
    S_0 = margin * volume * ppu;

    // Number of jumps.
    int n;
    std::cin >> n;
    std::vector<double> sec_levels(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> sec_levels[i];
    }
}
