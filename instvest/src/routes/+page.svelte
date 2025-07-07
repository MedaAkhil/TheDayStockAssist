<script lang="ts">
	import { onMount } from 'svelte';

	let nseData: any[] = [];
	let error: string | null = null;

	onMount(async () => {
		try {
			// const response = await fetch('https://thedaystockassist.onrender.com/nse');
			const response = await fetch("http://localhost:3000/nse");
			if (!response.ok) {
				throw new Error(`HTTP error! status: ${response.status}`);
			}
			const rawData = await response.json();

			// Check if it's a string, then parse it
			if (typeof rawData === 'string') {
				nseData = JSON.parse(rawData);
			} else {
				nseData = rawData;
			}
		} catch (e: any) {
			error = e.message;
		}
	});
</script>

<style>
	table {
		width: 100%;
		border-collapse: collapse;
		margin-top: 1rem;
		font-family: sans-serif;
	}

	th, td {
		border: 1px solid #ddd;
		padding: 8px;
		text-align: left;
	}

	th {
		background-color: #2c3e50;
		color: white;
	}

	tr:nth-child(even) {
		background-color: #f2f2f2;
	}

	tr:hover {
		background-color: #ddd;
	}
</style>

<h1>NSE Stock Growth Data</h1>

{#if error}
	<p style="color: red;">Error: {error}</p>
{:else if !nseData || nseData.length === 0}
	<p>Loading...</p>
{:else}
	<table>
		<thead>
			<tr>
				<th>Stock Symbol</th>
				<th>Stock Name</th>
				<th>Growth Rate (%)</th>
			</tr>
		</thead>
		<tbody>
			{#each nseData as stock}
				<tr>
					<td>{stock.stock_symbol}</td>
					<td>{stock.stock_name}</td>
					<td>
						{#if stock.growth_rate_percent !== null}
							{stock.growth_rate_percent}%
						{:else}
							<span style="color: gray;">N/A</span>
						{/if}
					</td>
				</tr>
			{/each}
		</tbody>
	</table>
{/if}
