<script>
	import "../app.css";
	let { children } = $props();
</script>

<nav class="flex justify-between items-center bg-gray-800 p-4">
	<div class="flex items-center">
		<a href="/" class="text-white text-lg font-bold hover:text-gray-300">Evidenca letenja</a>
		<a href="/mojiLeti" class="ml-4 text-white hover:text-gray-300">Moji leti</a>
		<a href="/zgodovina" class="ml-4 text-white hover:text-gray-300">Zgodovina</a>
		<a href="/letala" class="ml-4 text-white hover:text-gray-300">Letala</a>
	</div>
</nav>

<main>
	{@render children()}
</main>
