import streamlit as st

# ─── Header ───────────────────────────────────────
st.title("⚙️ Mechanical Unit Converter & Material Density Checker")
st.markdown("**Name:** Syed Talha Umar &nbsp;&nbsp;|&nbsp;&nbsp; **Roll No:** 25-ME-99")
st.markdown("---")

# ─── UNIT CONVERTER ───────────────────────────────
st.header("🔄 Unit Converter")

category = st.selectbox("Select Category", ["Length", "Mass", "Pressure", "Temperature", "Force"])

def convert(category, value, from_unit, to_unit):
    conversions = {
        "Length": {"m": 1, "cm": 100, "mm": 1000, "km": 0.001, "ft": 3.28084, "inch": 39.3701},
        "Mass":   {"kg": 1, "g": 1000, "mg": 1e6, "lb": 2.20462, "ton": 0.001},
        "Pressure": {"Pa": 1, "kPa": 0.001, "MPa": 1e-6, "bar": 1e-5, "psi": 0.000145038},
        "Force":  {"N": 1, "kN": 0.001, "lbf": 0.224809, "kgf": 0.101972},
    }
    if category == "Temperature":
        if from_unit == "°C" and to_unit == "°F": return value * 9/5 + 32
        if from_unit == "°F" and to_unit == "°C": return (value - 32) * 5/9
        if from_unit == "°C" and to_unit == "K":  return value + 273.15
        if from_unit == "K"  and to_unit == "°C": return value - 273.15
        if from_unit == "°F" and to_unit == "K":  return (value - 32) * 5/9 + 273.15
        if from_unit == "K"  and to_unit == "°F": return (value - 273.15) * 9/5 + 32
        return value
    units = conversions[category]
    return value / units[from_unit] * units[to_unit]

units_map = {
    "Length":      ["m", "cm", "mm", "km", "ft", "inch"],
    "Mass":        ["kg", "g", "mg", "lb", "ton"],
    "Pressure":    ["Pa", "kPa", "MPa", "bar", "psi"],
    "Temperature": ["°C", "°F", "K"],
    "Force":       ["N", "kN", "lbf", "kgf"],
}

units = units_map[category]
col1, col2, col3 = st.columns(3)
with col1: value = st.number_input("Enter Value", value=1.0)
with col2: from_unit = st.selectbox("From", units)
with col3: to_unit = st.selectbox("To", units)

if st.button("Convert ⚡"):
    result = convert(category, value, from_unit, to_unit)
    st.success(f"✅ {value} {from_unit} = **{result:.4f} {to_unit}**")

st.markdown("---")

# ─── MATERIAL DENSITY CHECKER ─────────────────────
st.header("🧱 Material Density Checker")

materials = {
    "Steel":        7850,
    "Aluminum":     2700,
    "Copper":       8960,
    "Brass":        8500,
    "Cast Iron":    7200,
    "Titanium":     4500,
    "Concrete":     2400,
    "Wood (Pine)":  530,
    "Rubber":       1200,
    "Glass":        2500,
    "Water":        1000,
    "Air":          1.225,
}

material = st.selectbox("Select Material", list(materials.keys()))
density = materials[material]
st.info(f"📦 Density of **{material}** = `{density} kg/m³`")

volume = st.number_input("Enter Volume (m³) to calculate mass", value=1.0, min_value=0.0001)
mass = density * volume
st.success(f"⚖️ Mass = {density} × {volume} = **{mass:.2f} kg**")

st.markdown("---")
st.caption("IMechE Design Challenge 2026 | Syed Talha Umar | 25-ME-99")
