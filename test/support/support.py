def sort(result):
	world_views = []
	for world_view in result:
		not_k = [x.name.replace('aux_not_','~') for x in world_view if 'aux_not_' in x.name]
		k = [x.name.replace('aux_','') for x in world_view if 'aux_not_' not in x.name]
		print(sorted(not_k)+sorted(k))
		world_views.append(sorted(not_k)+sorted(k))

	return sorted(world_views)


def formalize(world_views):
	world_views = sort(world_views)
	result = ('%s' % world_views).replace('\'','').replace(' ','')

	return result
