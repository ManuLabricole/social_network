<template>
	<div class="flex items-center space-x-2">
		<div v-if="isFriend">
			<button
				class="flex align-item py-4 px-6 bg-gray-500 text-white rounded-lg hover:bg-gray-700">
				<span class="material-icons text-red-700 mr-4"> person_remove </span>
				Remove
			</button>
		</div>

		<!-- Check if request is pending, display pending icon and disable button -->
		<div
			v-else-if="isRequestPending"
			class="flex items-center space-x-1 text-gray-500">
			<span class="material-icons"> pending </span>

			<span>Pending</span>
		</div>

		<!-- Display send icon and button if not already friends or request is not pending -->
		<button
			v-if="!isFriend"
			@click="sendFriendRequest"
			class="flex items-center inline-block py-4 px-6 bg-purple-600 text-white rounded-lg">
			<span class="material-icons mr-4">group_add</span>
			Send Request
		</button>
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
