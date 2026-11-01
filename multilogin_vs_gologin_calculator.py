#!/usr/bin/env python3
"""Multilogin vs GoLogin Enterprise Fingerprint Pricing Calculator 2026."""
import argparse

def calculate(profiles=300):
    # Multilogin Team: ~€199/mo (~$215/mo) or ~$199/mo for 300 profiles. Annual 25% off -> ~$149.25/mo ($1791/yr).
    ml_monthly = 199.0
    ml_annual_monthly = 149.25
    ml_annual_total = ml_annual_monthly * 12.0

    # GoLogin Business: $99.00/mo for 300 profiles. 50% annual off -> $49.50/mo ($594/yr).
    gl_monthly = 99.0
    gl_annual_monthly = 49.50
    gl_annual_total = gl_annual_monthly * 12.0

    annual_delta = ml_annual_total - gl_annual_total
    monthly_delta = ml_annual_monthly - gl_annual_monthly

    print("=" * 65)
    print(f"Multilogin vs GoLogin: 300 Profiles Enterprise Comparison")
    print("=" * 65)
    print(f"Multilogin Team (Annual):  ${ml_annual_monthly:.2f}/mo (${ml_annual_total:.2f}/yr)")
    print(f"GoLogin Business (Annual): ${gl_annual_monthly:.2f}/mo (${gl_annual_total:.2f}/yr)")
    print(f"Monthly Cost Difference:   ${monthly_delta:.2f}/mo")
    print(f"Annual Capital Saved:      ${annual_delta:.2f}/yr with GoLogin")
    print("=" * 65)
    return gl_annual_total, ml_annual_total, annual_delta

if __name__ == "__main__":
    calculate()
