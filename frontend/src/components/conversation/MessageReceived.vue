<template>
	<div class="flex w-full mt-2 space-x-3 max-w-md">
		<div class="flex-shrink-0 h-10 w-10 rounded-full bg-gray-300">
			<img
				src="https://i.pravatar.cc/300?img=70"
				class="w-[40px] rounded-full" />
		</div>
		<div>
			<div class="bg-gray-300 p-3 rounded-r-lg rounded-bl-lg">
				<p class="text-sm">
					Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
					eiusmod tempor incididunt ut labore et dolore magna aliqua.
				</p>
			</div>
			<span class="text-xs text-gray-500 leading-none">2 min ago</span>
		</div>
	</div>
</template>

<script>
	export default {
		name: 'MessageReceived',
		setup() {
			return {};
		},
	};
</script>

<style scoped></style>
