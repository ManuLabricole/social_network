<template>
	<div
		class="p-4 space-y-4 bg-white border border-gray-200 text-center rounded-lg">
		<p class="text-sm font-bold"><strong>Friend Requests</strong></p>
	</div>
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
				const response = await axios
					.get('/api/friendship-requests')
					.then((response) => {
						console.log(response);
						this.pendingRequests = response.data;
						console.log(this.pendingRequests);
					})
					.catch((error) => {
						console.log(error);
					});
			},
		},
		mounted() {
			this.fetchPendingRequests();
		},
	};
</script>

<style></style>
