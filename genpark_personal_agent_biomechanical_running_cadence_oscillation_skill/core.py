# -*- coding: utf-8 -*-
"""Biomechanical Running Cadence & Oscillation Analyzer for GenPark Personal Agent."""
import json
from typing import Dict, Any

class BiomechanicalRunningCadenceOscillationAnalyzer:
    @staticmethod
    def analyze_running_efficiency_kinematics(step_cadence_spm: int, vertical_oscillation_cm: float, ground_contact_time_ms: int) -> Dict[str, Any]:
        # Stride length proxy: at 10 km/h (~166.7 m/min), stride = 166.7 / spm
        # Vertical Ratio = (Vertical Oscillation / Stride Length) * 100
        estimated_stride_cm = max(50.0, (166.67 / max(100, step_cadence_spm)) * 100.0)
        vertical_ratio_pct = round((vertical_oscillation_cm / estimated_stride_cm) * 100.0, 1)
        
        tier = "ELITE_EFFICIENCY" if vertical_ratio_pct < 6.5 and step_cadence_spm >= 175 else ("GOOD_FORM" if vertical_ratio_pct < 8.5 else "EXCESSIVE_BOUNCE_BRAKING")
        braking_force_proxy = "HIGH" if ground_contact_time_ms > 260 else ("MODERATE" if ground_contact_time_ms > 220 else "ELITE_ELASTIC_RECOIL")
        
        return {
            "cadence_spm": step_cadence_spm,
            "vertical_oscillation_cm": vertical_oscillation_cm,
            "ground_contact_time_ms": ground_contact_time_ms,
            "vertical_ratio_pct": vertical_ratio_pct,
            "running_economy_tier": tier,
            "impact_braking_assessment": braking_force_proxy
        }

    @staticmethod
    def prescribe_cadence_form_drill_remedy(current_spm: int, vertical_ratio_pct: float = 9.0) -> Dict[str, Any]:
        target_spm = min(182, current_spm + 8)
        drills = [
            f"Set acoustic audio metronome to {target_spm} BPM during warm-up intervals",
            "A-Skips and B-Skips: 3 x 30m focusing on rapid foot pull beneath center of mass",
            "Hill sprints (6-8 degree gradient) to naturally enforce high cadence and forward lean"
        ]
        return {"current_spm": current_spm, "target_target_spm": target_spm, "prescribed_drills": drills, "injury_prevention_benefit": "Reduces knee patellofemoral compressive force by up to 22%."}
