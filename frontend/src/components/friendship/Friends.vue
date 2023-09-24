<template>
	<div><h1>Friends</h1></div>
	<div
		v-for="friend in friends"
		:key="friend"
		class="flex items-center justify-between p-2 border-b border-gray-200">
		<div class="flex items-center space-x-4">
			<img
				src="https://i.pravatar.cc/50?img=70"
				class="w-10 h-10 rounded-full" />
			<p class="font-medium">{{ friend.user.name }}</p>
		</div>
		<div class="flex items-center space-x-4">
			<button
				@click="removeFriendship(friend)"
				class="flex items-center pr-2 pl-2 bg-gray-300 rounded-full hover:bg-red-500 focus:outline-none focus:ring focus:ring-red-200">
				<p class="m-0 mr-1">remove</p>
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
</template>

<script>
	import { useUserStore } from '../../stores/user';
	import axios from 'axios';
	export default {
		setup() {
			return {
				userStore: useUserStore(),
			};
		},
		data() {
			return {
				userId: this.userStore.user.id,
				friends: [],
			};
		},
		mounted() {
			this.fetchFriends();
		},
		methods: {
			async fetchFriends() {
				try {
					const response = await axios.get(`/api/v1/users/me/friends/`); // Adjust the URL if needed
					console.log('Friends:', response);
					this.friends = response.data;
				} catch (error) {
					console.error('Error fetching friends:', error);
				}
			},
		},
	};
</script>
