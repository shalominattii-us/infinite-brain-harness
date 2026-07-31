"""
AEGENTIX CYBERNETICS - REAL-TIME CYBERDEX STREAM RUNNER
=========================================================
Generates continuous live telemetry streams (OSINT, DFIR, SaaS Control, MITRE ATT&CK)
and observes Cyberdex model triaging & SOAR automated remediations in real time.
"""

import os
import sys
import time
import json
import random
import datetime

# Fix Windows console UTF-8 output encoding if needed
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

from omni_cyberdex_harness import OmniCyberdexModel

# Sample Cyberdex Threat Telemetry Stream Sources
THREAT_INDICATORS = [
    {"domain": "sovereign-os", "severity": "P1", "indicator": "okta-auth-bypass-attempt", "mitre": "T1528", "action": "REVOKE_OAUTH_REFRESH_TOKEN"},
    {"domain": "aegentix-trading", "severity": "P1", "indicator": "coinbase-cdp-killswitch-tripped", "mitre": "T1078", "action": "ENGAGE_KILLSWITCH_LOCKDOWN"},
    {"domain": "cloudshell-organizer", "severity": "P2", "indicator": "unregistered-ip-access", "mitre": "T1078", "action": "QUARANTINE_IP"},
    {"domain": "vector-memory", "severity": "P2", "indicator": "high-entropy-vector-query-spike", "mitre": "T1567", "action": "THROTTLE_RATE_LIMIT"},
    {"domain": "identity-os", "severity": "P3", "indicator": "did-signature-verification-warning", "mitre": "T1528", "action": "LOG_AUDIT_TRAIL"},
    {"domain": "xr-spatial", "severity": "P4", "indicator": "metaverse-telemetry-heartbeat-ok", "mitre": "NONE", "action": "NO_ACTION_REQUIRED"}
]

def run_live_cyberdex_stream(iterations: int = 15, delay_sec: float = 0.5):
    print("=" * 75)
    print("🚀 [AEGENTIX CYBERNETICS] STARTING LIVE CYBERDEX EVENT STREAM")
    print("=" * 75)
    
    model = OmniCyberdexModel("Omni-Cyberdex-LiveStream")
    print(f"[*] Initialized Cyberdex Model: {model.name} (v{model.version})")
    print(f"[*] Subscribed to Event Topics: OSINT, DFIR, SaaS Control, SOAR")
    print(f"[*] Observer Stream Active | Iterations: {iterations} | Stream Delay: {delay_sec}s")
    print("-" * 75)
    
    for i in range(1, iterations + 1):
        event = random.choice(THREAT_INDICATORS)
        timestamp = datetime.datetime.now(datetime.timezone.utc).strftime("%H:%M:%S.%f")[:-3]
        
        # Execute Cyberdex Triaging
        res = model.execute_cyberdex_cycle(event)
        
        # Format Live Stream Log Output
        sev_tag = f"[{event['severity']}]"
        
        print(f"[{timestamp}] Event #{i:02d} | {sev_tag:<4} | Domain: {event['domain']:<22} | IOC: {event['indicator']:<32} | MITRE: {event['mitre']:<5} | Action: {event['action']}")
        sys.stdout.flush()
        time.sleep(delay_sec)
        
    print("-" * 75)
    print("✅ [CYBERDEX STREAM COMPLETED] All telemetry cycles processed cleanly.")
    print(f"📊 Final Model State: {json.dumps(model.get_status(), indent=2)}")
    print("=" * 75)

if __name__ == "__main__":
    count = int(sys.argv[1]) if len(sys.argv) > 1 else 15
    run_live_cyberdex_stream(iterations=count, delay_sec=0.4)
