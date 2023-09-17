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
	export default {
		setup() {
			return {};
		},
		components: {
			FeedItem,
		},
	};
</script>

<style lang="scss" scoped></style>
