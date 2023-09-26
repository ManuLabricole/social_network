<template>
	<div class="flex items-center space-between">
		<div v-if="isFriend">
			<button
				class="flex align-item mr-4 py-2 px-4 bg-gray-500 text-white rounded-lg hover:bg-gray-700 hover:text-red-500">
				<span class="material-icons mr-2"> person_remove </span>
				Remove
			</button>
		</div>

		<button
			v-else-if="!isFriend"
			@click="sendFriendRequest"
			class="flex items-center inline-block py-2 px-4 bg-purple-600 text-white rounded-lg">
			<span class="material-icons mr-4">group_add</span>
			add
		</button>
		<!--
		<div
			v-else-if="isRequestPending"
			class="flex items-center space-x-1 text-gray-500">
			<button
				class="flex align-item py-4 px-6 bg-gray-500 text-white rounded-lg hover:bg-gray-700 opacity-50 cursor-not-allowed pointer-events-none"
				disabled>
				<span class="material-icons mr-4"> pending </span>
				<span>pending...</span>
			</button>
		</div> -->
	</div>
</template>

<script>
	import axios from 'axios';
	export default {
		name: 'SendRequest',
		props: {
			profile: {
				type: Object,
				required: true,
			},
		},
		data() {
			return {
				isFriend: false,
				isRequestPending: false,
			};
		},
		mounted() {
			this.checkFriendshipStatus();
		},
		methods: {
			checkFriendshipStatus() {
				axios
					.get(`/api/v1/users/friendship/status/${this.profile.user.id}`)
					.then((response) => {
						console.log(response);
					})
					.catch((error) => {
						console.log(error);
					});
			},
		},
	};
</script>
