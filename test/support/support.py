def sort(result):
    world_views = []
    for world_view in result:
        not_k, not_sn_k, sn_k, k = [], [], [], []
        for literal in world_view:
            if 'aux_not_' in literal.name:
                symbol = literal.name.replace('aux_not_', '~')
                if 'sn_' in symbol:
                    symbol = symbol.replace('sn_', ' -')
                    if literal.arguments:
                        arguments = [argument.name for argument in literal.arguments]
                        not_sn_k.append('%s(%s)' % (symbol, (', ').join(arguments)))
                    else:
                        not_sn_k.append(symbol)
                else:
                    if literal.arguments:
                        arguments = [argument.name for argument in literal.arguments]
                        not_k.append('%s(%s)' % (symbol, (', ').join(arguments)))
                    else:
                        not_k.append(symbol)
            elif 'aux_' in literal.name:
                symbol = literal.name.replace('aux_', '')
                if 'sn_' in literal.name:
                    symbol = symbol.replace('sn_', ' -')
                    if literal.arguments:
                        arguments = [argument.name for argument in literal.arguments]
                        sn_k.append('%s(%s)' % (symbol, (', ').join(arguments)))
                    else:
                        sn_k.append(symbol)
                else:
                    if literal.arguments:
                        arguments = [argument.name for argument in literal.arguments]
                        k.append('%s(%s)' % (symbol, (', ').join(arguments)))
                    else:
                        k.append(symbol)

        world_views.append(sorted(not_k)+sorted(not_sn_k)+sorted(sn_k)+sorted(k))

    return sorted(world_views)


def formalize(world_views):
    world_views = sort(world_views)
    result = ('%s' % world_views).replace('\'', '').replace(' ', '')

    return result
