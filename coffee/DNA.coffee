
class ConnectionOperator
    # definition of regulator of a protein connection
    constructor: (fromCode, toCode, operatorBehavior) ->
        # :param fromCode: proteinCode connection is from
        # :param toCode: proteinCode connection is to
        # :operatorBehavior: string which identifies the behavior of the operator
        operators = ['silencer']
        if operatorBehavior in operators
            @operator = operatorBehavior
            @from = fromCode
            @to = toCode
        else
            throw Error('operatorBehavior not recognized')


class ProteinNode
    # protein node in a gene regulatory network
    constructor: (proteinCode) ->
        @proteinCode = proteinCode
        @connections = []  # list of proteinCodes which this connects to (ie: what does this activate)
        @silences = []  # list of connections silenced by this node {from:'code1', to:'code2'}

class DNA
    # a representation of the gene regulatory network typically encoded as DNA
    constructor: (parents, doNotGenerate=false) ->
        @_nodes = []  # aka proteins
        if doNotGenerate
            return
        else if parents?
            # TODO: inherit
            console.log('inheriting...')
        else
            # TODO: make random DNA
            console.log('randomness')

    clone: () ->
        # returns a perfect clone of the DNA object
        newDNA = new DNA([], true)
        for node in dna.nodes
            newDNA.nodes.push(node.clone())

        return newDNA

    getProteinResponse: (inputProtein) ->
        # returns a list of genes which are activated in response to the given inputProtein
        # TODO: retrieve input protein node & return connections
        return ['NotImp']  # Not Yet Implemented Protein response

    connectionSilencedBy: (inProtein, outProtein, proteinList) ->
        # returns true if any proteins in the proteinList silence the inProtein->outProtein link
        return false

module.exports = DNA