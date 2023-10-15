<template>
	<div class="flex w-full mt-2 space-x-3 max-w-md ml-auto justify-end">
		<div
			class="bg-blue-600 text-white p-3 rounded-l-lg rounded-br-lg max-w-[100%] whitespace-normal">
			<p class="text-sm break-words">Message sent !</p>
		</div>
		<span
			class="text-xs text-gray-500 leading-none absolute bottom-0 left-0 ml-3 mb-2"
			>2 min ago</span
		>

		<div class="flex-shrink-0 h-10 w-10 rounded-full bg-gray-300">
			<img
				src="https://i.pravatar.cc/300?img=70"
				class="w-10 h-10 rounded-full" />
		</div>
	</div>
</template>

<script>
export default {
        name: 'MessageSent',
    };
</script>

<style scoped></style>
