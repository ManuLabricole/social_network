<template>
	<div
		class="p-4 space-y-4 bg-white border border-gray-200 text-center rounded-lg">
		<p class="text-sm font-bold"><strong>Friend Requests</strong></p>
		<div
			v-for="request in pendingRequests"
			:key="request.id"
			class="flex items-center justify-between p-2 border-b border-gray-200">
			<div class="flex items-center space-x-2">
				<!-- Avatar -->
				<img
					src="https://i.pravatar.cc/50?img=70"
					class="w-10 h-10 rounded-full" />
				<!-- Sender's Name -->
				<p class="font-medium">{{ request.sender.user.name }}</p>
				<!-- <p class="text-xs text-gray-500">{{ request.id}}</p> -->
			</div>
			<div class="flex space-x-2">
				<button
					class="p-2 bg-green-500 rounded-full hover:bg-green-600 focus:outline-none focus:ring focus:ring-green-200"
					@click="updateFriendRequest(request.id, 'ACCEPTED')">
					<svg
						xmlns="http://www.w3.org/2000/svg"
						class="h-5 w-5 text-white"
						viewBox="0 0 20 20"
						fill="currentColor">
						<path
							fill-rule="evenodd"
							d="M6.293 9.293a1 1 0 011.414 0L10 11.586l2.293-2.293a1 1 0 111.414 1.414l-3 3a1 1 0 01-1.414 0l-3-3a1 1 0 010-1.414z"
							clip-rule="evenodd" />
					</svg>
				</button>
				<button
					class="p-2 bg-red-500 rounded-full hover:bg-red-600 focus:outline-none focus:ring focus:ring-red-200"
					@click="updateFriendRequest(request.id, 'DECLINED')">
					<svg
						xmlns="http://www.w3.org/2000/svg"
						class="h-5 w-5 text-white"
						viewBox="0 0 20 20"
						fill="currentColor">
						<path
							fill-rule="evenodd"
							d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
							clip-rule="evenodd" />
					</svg>
				</button>
			</div>
		</div>
	</div>
</template>

<script>
	import axios from 'axios';
	import { useUserStore } from '../../stores/user';

	export default {
		setup() {
			return {};
		},
		data() {
			return {
				pendingRequests: [],
			};
		},
		mounted() {
			this.fetchPendingRequests();
		},
		methods: {
			async fetchPendingRequests() {
				console.log('fetchPendingRequests()');
				try {
					const response = await axios.get(
						'/api/v1/users/friend-requests/pending/'
					);
					this.pendingRequests = response.data;
				} catch (error) {
					console.log(error);
				}
			},
			updateFriendRequest(requestId, requestType) {
				console.log(requestId);
				axios
					.post(`/api/v1/users/friend-requests/${requestId}/`, {
						status: requestType,
					})
					.then((response) => {
						console;
						this.fetchPendingRequests();
					})
					.catch((error) => {
						console.log(error);
					});
			},
		},
	};
</script>

<style></style>
