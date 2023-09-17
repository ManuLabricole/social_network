<template>
	<div class="main-center col-span-2 space-y-4">
		<FeedItem
			v-for="post in posts"
			:key="post.id"
			:post="post" />
	</div>
</template>

<script>
	import FeedItem from '../../components/feed/FeedItem.vue';
	import axios from 'axios';
	export default {
		components: {
			FeedItem,
		},
		props: {
			profile: {
				type: Object,
				required: true,
			},
		},
		data() {
			return {
				posts: [],
			};
		},
		mounted() {
			this.getPostsByUserId();
		},
		methods: {
			getPostsByUserId() {
				axios
					.get(`/api/v1/posts/user/${this.profile.id}/`)
					.then((response) => {
						this.posts = response.data;
					})
					.catch((error) => {
						console.error(error);
						console.warn('Error getting feed');
					});
			},
		},
		watch: {
			profile() {
				this.getPostsByUserId();
			},
		},
	};
</script>

<style lang="scss" scoped></style>
