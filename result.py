import time
import matplotlib.pyplot as plt

# ✅ IMPORT FROM CORRECT FILE
from ring_signature import generate_voter_keypair, ring_sign, ring_verify, hash_mod_p


def benchmark(voter_counts):
    results = []

    for count in voter_counts:
        print(f"Benchmarking {count} voters...")

        # 1. Key Generation Time
        start = time.perf_counter()
        keys = [generate_voter_keypair() for _ in range(count)]
        pks = [k[1] for k in keys]
        end = time.perf_counter()
        kg_time = (end - start) * 1000

        # 2. Signature Generation Time
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


# ---------------- RUN ----------------
voter_counts = [10, 50, 100, 200]
results = benchmark(voter_counts)

# ---------------- EXTRACT ----------------
voters = [r["voters"] for r in results]
keygen_time = [r["keygen"] for r in results]
sign_time = [r["sign"] for r in results]
verify_time = [r["verify"] for r in results]
total_time = [r["total"] for r in results]


# ---------------- GRAPH 1 ----------------
plt.figure(figsize=(10, 6))

plt.plot(voters, keygen_time, label='Key Generation', marker='o')
plt.plot(voters, sign_time, label='Ring Signing', marker='s')
plt.plot(voters, verify_time, label='Ring Verification', marker='^')

plt.title('Performance Analysis vs Number of Voters')
plt.xlabel('Number of Voters')
plt.ylabel('Time (ms)')
plt.grid(True)
plt.legend()

plt.savefig('performance_analysis.png', dpi=300)
plt.show()


# ---------------- GRAPH 2 ----------------
plt.figure(figsize=(10, 6))

plt.plot(voters, total_time, label='Total Execution Time', marker='D')

plt.title('Total Execution Time vs Voters')
plt.xlabel('Number of Voters')
plt.ylabel('Time (ms)')
plt.grid(True)
plt.legend()

plt.savefig('total_execution_time.png', dpi=300)
plt.show()

print("Graphs generated successfully ✅")