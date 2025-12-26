import argparse
from .pricer import MonteCarloPricer
from .payoffs import EuropeanCall

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--s", type=float, required=True)
    parser.add_argument("--k", type=float, required=True)
    parser.add_argument("--r", type=float, required=True)
    parser.add_argument("--sigma", type=float, required=True)
    parser.add_argument("--t", type=float, required=True)
    parser.add_argument("--paths", type=int, required=True)
    parser.add_argument("--vr", action="append", default=[])

    args = parser.parse_args()

    pricer = MonteCarloPricer(
        args.s, args.r, args.sigma, args.t, args.paths
    )

    mean, n, std, stderr, ci = pricer.price(
        EuropeanCall(args.k),
        antithetic="antithetic" in args.vr,
        control_variate="control_variate" in args.vr
    )

    print(f"price={mean:.2f}")
    print(f"n={n} std={std:.2f} stderr={stderr:.5f}")
    print(f"95% CI: [{ci[0]:.2f}, {ci[1]:.2f}]")

if __name__ == "__main__":
    main()
