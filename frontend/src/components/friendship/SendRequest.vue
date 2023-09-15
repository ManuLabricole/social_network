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
			<button
				class="flex align-item py-4 px-6 bg-gray-500 text-white rounded-lg hover:bg-gray-700 opacity-50 cursor-not-allowed pointer-events-none"
				disabled>
				<span class="material-icons mr-4"> pending </span>
				<span>Pending Invitation</span>
			</button>
		</div>

		<!-- Display send icon and button if not already friends or request is not pending -->
		<button
			v-else-if="!isFriend"
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
		watch: {
			isFriend() {
				console.log('isFriend changed');
			},
			isRequestPending() {
				console.log('isRequestPending changed');
			},
		},

		mounted() {
			console.log('isFriend', this.isFriend);
			console.log('isRequestPending', this.isRequestPending);
			console.log('isMyProfile', this.isMyProfile);
			console.log('mounyted');
		},

		methods() {},
	};
</script>

<style lang="postcss" scoped></style>
