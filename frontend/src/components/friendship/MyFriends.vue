<template>
	<div><h1>MyFriends</h1></div>
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
				friends: [],
			};
		},
		mounted() {
			this.fetchFriends();
		},
		methods: {
			async fetchFriends() {
				try {
					const response = await axios.get('/api/v1/friend-requests/get-friends/'); // Adjust the URL if needed
					this.friends = response;
				} catch (error) {
					console.error('Error fetching friends:', error);
				}
			},
		},
	};
</script>
