<template>
	<div
		class="p-4 bg-white border border-gray-200 rounded-lg"
		v-if="isFetched">
		<h3 class="mb-6 text-xl">Trends</h3>
		<div
			class="space-y-4"
			v-for="trend in trends"
			:key="trend.id">
			<div class="flex items-center justify-between mb-6">
				<div class="flex items-center space-x-2">
					<p class="text-xs">
						<strong>#{{ trend.hashtag }}</strong
						><br />
						<span class="text-gray-500">{{ trend.count }} posts</span>
					</p>
				</div>
				<a
					href="#"
					class="py-2 px-3 bg-purple-600 text-white text-xs rounded-lg"
					>Explore</a
				>
			</div>
		</div>
	</div>
</template>

<script>
	import axios from 'axios';
	export default {
		data() {
			return {
				trends: [],
				isFetched: false,
			};
		},

		mounted() {
			this.fetchTrends();
		},
		methods: {
			fetchTrends() {
				axios
					.get(`/api/v1/posts/trends`)
					.then((response) => {
						this.trends = response.data;
						this.isFetched = true;
						console.log('isFetched', this.isFetched);
					})
					.catch((error) => {
						console.log(error);
					});
			},
		},
	};
</script>

<style lang="postcss" scoped></style>
