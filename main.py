from volatility_engine import VolatilityEngine
from structure_engine import StructureEngine
from liquidity_engine import LiquidityEngine
from options_engine import OptionsEngine

def main():

    print("Starting Volatility-First Trading System...")

    # Placeholder candle data
    candles = [
        {"high": 100, "low": 95, "close": 98},
        {"high": 102, "low": 96, "close": 101}
    ]

    vol_engine = VolatilityEngine()
    struct_engine = StructureEngine()
    liq_engine = LiquidityEngine()
    opt_engine = OptionsEngine()

    iv_pct = vol_engine.iv_percentile(0.25, [0.2, 0.3, 0.4, 0.5])

    structure = struct_engine.detect_structure(candles)
    sweep = liq_engine.detect_sweep(candles)

    print("IV Percentile:", iv_pct)
    print("Structure:", structure)
    print("Liquidity Sweep:", sweep)

    print("System initialized successfully.")

if __name__ == "__main__":
    main()
