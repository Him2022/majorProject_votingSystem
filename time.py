import time
import matplotlib.pyplot as plt
from ring_signature import generate_voter_keypair, ring_sign, ring_verify, hash_mod_p

def benchmark_voters(voter_counts):
    results = []
    
    for count in voter_counts:
        print(f"Benchmarking {count} voters...")
        
        # 1. Key Gen Time
        start = time.perf_counter()
        keys = [generate_voter_keypair() for _ in range(count)]
        pks = [k[1] for k in keys]
        end = time.perf_counter()
        kg_time = (end - start) * 1000 # ms
        
        # 2. Signature Gen Time (for one voter)
        msg_hash = hash_mod_p("sample_vote")
        start = time.perf_counter()
        sig = ring_sign(msg_hash, pks, 0, keys[0][0])
        end = time.perf_counter()
        sg_time = (end - start) * 1000
        
        # 3. Verification Time
        start = time.perf_counter()
        ring_verify(msg_hash, sig, pks)
        end = time.perf_counter()
        sv_time = (end - start) * 1000
        
        results.append({
            "voters": count,
            "keygen": kg_time,
            "sign": sg_time,
            "verify": sv_time,
            "total": kg_time + sg_time + sv_time
        })
    return results

# Run for 10, 50, 100, 200 voters
counts = [10, 50, 100, 200]
data = benchmark_voters(counts)

# Print for your Research Paper Table
print("\n--- RESULTS TABLE ---")
print("Voters | KeyGen(ms) | Sign(ms) | Verify(ms) | Total(ms)")
for d in data:
    print(f"{d['voters']:<7} | {d['keygen']:<10.2f} | {d['sign']:<8.2f} | {d['verify']:<10.2f} | {d['total']:.2f}")