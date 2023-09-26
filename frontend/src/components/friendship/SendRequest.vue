<template>
	<div
		v-if="isRequestChecked"
		class="flex items-center space-between">
		<div v-if="requestStatus == 'ACCEPTED'">
			<button
				@click="removeFriend"
				class="flex align-item mr-4 py-2 px-4 bg-gray-500 text-white rounded-lg hover:bg-gray-700 hover:text-red-500">
				<span class="material-icons mr-2"> person_remove </span>
				Remove
			</button>
		</div>
		<div v-else-if="requestStatus == 'PENDING' && requestType == 'SENT'">
			<button
				disabled
				class="flex items-center inline-block py-1 px-2 mr-4 bg-gray-400 text-white rounded-lg cursor-not-allowed opacity-75">
				<span class="material-icons mr-4">check_circle</span>
				Request Sent
			</button>
		</div>
		<div v-else-if="requestStatus == 'PENDING' && requestType == 'RECEIVED'">
			<button
				@click="acceptFriendRequest('ACCEPTED')"
				class="flex items-center inline-block py-1 px-2 mr-4 bg-green-600 text-white rounded-lg">
				<span class="material-icons mr-4">group_add</span>
				accept
			</button>
		</div>
		<div v-else>
			<button
				@click="sendFriendRequest"
				class="flex items-center inline-block mr-4 py-1 px-2 bg-purple-600 text-white rounded-lg">
				<span class="material-icons mr-4">group_add</span>
				add
			</button>
		</div>
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
				isRequestChecked: false,
				requestType: '',
				requestStatus: '',
			};
		},
		mounted() {
			this.checkFriendshipStatus();
		},
		methods: {
			checkFriendshipStatus() {
				axios
					.get(`/api/v1/users/friendship/${this.profile.user.id}/status`)
					.then((response) => {
						this.requestStatus = response.data.status;
						this.requestType = response.data.request;
						this.isRequestChecked = true;
						console.log(response.data);
					})
					.catch((error) => {
						console.log(error);
					});
			},
			acceptFriendRequest(requestType) {
				axios
					.put(`/api/v1/users/friendship/requests/${this.profile.user.id}/`, {
						status: requestType,
					})
					.then((response) => {
						console.log(response.data);
						this.checkFriendshipStatus();
					})
					.catch((error) => {
						console.log(error);
					});
			},
			removeFriend() {
				axios
					.delete(`/api/v1/users/friendship/requests/${this.profile.user.id}/`)
					.then((response) => {
						console.log(response.data);
						this.checkFriendshipStatus();
					})
					.catch((error) => {
						console.log(error);
					});
			},
		},
	};
</script>
