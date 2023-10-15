<template>
	<div class="flex items-center justify-between mt-2">
		<div class="flex items-center space-x-2">
			<img
				src="https://i.pravatar.cc/300?img=70"
				class="w-[40px] rounded-full" />

			<p class="text-xs"><strong>Code With Stein</strong></p>
		</div>
		<span class="text-xs text-gray-500">18 minutes ago</span>
	</div>
</template>

<script>
	export default {
		name: 'ConversationDetails',
		props: {
			conversation: {
				type: Object,
				required: true,
			},
		},
	};
</script>

<style scoped></style>
