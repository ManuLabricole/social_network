<template>
	<div><h1>MyFriends</h1></div>
</template>

<script>
	export default {
		setup() {
			return {};
		},
		data() {
			return {
				pendingRequests: [],
			};
		},
		methods: {
			async fetchPendingRequests() {
				try {
					const response = await axios.get('/api/v1/friend-requests/', {
						params: {
							request_type: 'accepted',
						},
					});
					console.log(response);
					this.pendingRequests = response.data;
					// console.log(this.pendingRequests);
				} catch (error) {
					console.log(error);
				}
			},
		},
	};
</script>
