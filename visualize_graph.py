import matplotlib.pyplot as plt

# Data points
voters = [10, 50, 100, 200]
keygen_time = [0.10, 0.31, 0.39, 0.78]
sign_time = [0.07, 0.03, 0.03, 0.04]
verify_time = [0.03, 0.03, 0.01, 0.02]
total_time = [0.20, 0.37, 0.43, 0.84]

# --- First Graph: Performance Analysis (Component breakdown only) ---
plt.figure(figsize=(10, 6))

plt.plot(voters, keygen_time, label='Key Generation', marker='o', linestyle='-', linewidth=2)
plt.plot(voters, sign_time, label='Ring Signing', marker='s', linestyle='--', linewidth=2)
plt.plot(voters, verify_time, label='Ring Verification', marker='^', linestyle='-.', linewidth=2)
# "Total Execution Time" line removed from this graph

plt.title('Performance Analysis: Computational Cost vs. Number of Voters', fontsize=14, fontweight='bold')
plt.xlabel('Number of Voters (Anonymity Set Size $N$)', fontsize=12)
plt.ylabel('Execution Time (ms)', fontsize=12)
plt.xticks(voters)
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend(loc='upper left', fontsize=10)
plt.tight_layout()

plt.savefig('performance_analysis.png', dpi=300)
plt.show() 

# --- Second Graph: System Scalability (Total Time only) ---
plt.figure(figsize=(10, 6))

plt.plot(voters, total_time, label='Total Execution Time', marker='D', color='black', linewidth=2.5)

plt.title('System Scalability: Total Execution Time vs. Voter Count', fontsize=14, fontweight='bold')
plt.xlabel('Number of Voters (Anonymity Set Size $N$)', fontsize=12)
plt.ylabel('Time (ms)', fontsize=12)
plt.xticks(voters)
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend(loc='upper left', fontsize=10)
plt.tight_layout()

plt.savefig('total_execution_time.png', dpi=300)
plt.show() 

print("Both graphs successfully generated and saved.")