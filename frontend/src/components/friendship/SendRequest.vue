<template>
	<div class="flex items-center space-x-2">
		<!-- Check if already friends, display rotated SVG -->
		<svg
			v-if="isFriend"
			class="w-6 h-6 text-green-500 transform rotate-45"
			fill="none"
			stroke="currentColor"
			viewBox="0 0 24 24"
			xmlns="http://www.w3.org/2000/svg">
			<path
				stroke-linecap="round"
				stroke-linejoin="round"
				stroke-width="2"
				d="M5 13l4 4L19 7"></path>
		</svg>

		<!-- Check if request is pending, display pending icon and disable button -->
		<div
			v-else-if="isRequestPending"
			class="flex items-center space-x-1 text-gray-500">
			<svg
				class="w-6 h-6"
				fill="none"
				stroke="currentColor"
				viewBox="0 0 24 24"
				xmlns="http://www.w3.org/2000/svg">
				<path
					stroke-linecap="round"
					stroke-linejoin="round"
					stroke-width="2"
					d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"></path>
			</svg>
			<span>Pending</span>
		</div>

		<!-- Display send icon and button if not already friends or request is not pending -->
		<div
			v-else
			@click="sendFriendRequest"
			class="cursor-pointer flex items-center space-x-1">
			<svg
				class="w-6 h-6 text-blue-500"
				fill="none"
				stroke="currentColor"
				viewBox="0 0 24 24"
				xmlns="http://www.w3.org/2000/svg">
				<path
					stroke-linecap="round"
					stroke-linejoin="round"
					stroke-width="2"
					d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"></path>
			</svg>
			<span class="text-blue-500">Send Request</span>
		</div>
	</div>
</template>

<script>
	export default {
		props: {
			isFriend: {
				type: Boolean,
				required: true,
			},
			isRequestPending: {
				type: Boolean,
				required: true,
			},
		},
		methods: {
			sendFriendRequest() {
				// Implement the logic to send a friend request
				// You can emit an event or call a method in the parent component here
			},
		},
	};
</script>

<style lang="postcss" scoped></style>
